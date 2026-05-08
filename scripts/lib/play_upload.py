#!/usr/bin/env python3
"""Upload an AAB to Google Play via the Android Publisher API.

Used by scripts/release-android.sh in place of `fastlane supply`.
"""

import argparse
import sys
import time

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


def upload(aab_path: str, package_name: str, track: str, json_key: str) -> int:
    credentials = service_account.Credentials.from_service_account_file(
        json_key, scopes=["https://www.googleapis.com/auth/androidpublisher"]
    )
    service = build("androidpublisher", "v3", credentials=credentials)
    edits = service.edits()

    print(f"Creating edit for {package_name}...")
    edit = edits.insert(packageName=package_name, body={}).execute()
    edit_id = edit["id"]

    try:
        print(f"Uploading {aab_path}...")
        media = MediaFileUpload(
            aab_path,
            mimetype="application/octet-stream",
            resumable=True,
        )
        bundle = edits.bundles().upload(
            packageName=package_name,
            editId=edit_id,
            media_body=media,
        ).execute()
        version_code = bundle["versionCode"]
        print(f"Uploaded versionCode {version_code}.")

        print(f"Assigning to track '{track}' as draft...")
        edits.tracks().update(
            packageName=package_name,
            editId=edit_id,
            track=track,
            body={
                "track": track,
                "releases": [
                    {
                        "status": "draft",
                        "versionCodes": [str(version_code)],
                    }
                ],
            },
        ).execute()

        print("Committing edit...")
        edits.commit(
            packageName=package_name,
            editId=edit_id,
            changesNotSentForReview=(track == "production"),
        ).execute()

        print(f"Uploaded {aab_path} to {package_name} on track '{track}' as draft.")
        return 0
    except HttpError as exc:
        print(f"Play API error: {exc}", file=sys.stderr)
        try:
            edits.delete(packageName=package_name, editId=edit_id).execute()
        except HttpError:
            pass
        return 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--aab", required=True)
    parser.add_argument("--package-name", required=True)
    parser.add_argument("--track", required=True)
    parser.add_argument("--json-key", required=True)
    args = parser.parse_args()
    return upload(args.aab, args.package_name, args.track, args.json_key)


if __name__ == "__main__":
    sys.exit(main())
