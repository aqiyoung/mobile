# App Store Submission

Reference for App Store Connect metadata and the resubmission flow after the 5.2.5 trademark rejection. All copy below is trademark-safe — no references to Apple product names (`Mac`, `macOS`, `iPhone`, `iPad`, etc.).

## Resubmission Checklist

1. Bump `expo.version` in `app.json` and `CFBundleShortVersionString` in `ios/Muxy/Info.plist` (current: `0.3.1`).
2. Update App Store Connect fields (Subtitle, Promotional Text, Description, Keywords, What's New, Review Notes) using the copy below.
3. Verify screenshots have no `Mac` / `macOS` text overlays.
4. Upload the new build (with the in-app string changes already merged).
5. Attach the demo video URL in Review Notes.
6. Submit for Review.
7. Reply to Apple's rejection thread with the message in the [Apple Reply](#apple-reply) section.

## Subtitle

App Store Connect → App Information → Subtitle (30 char max).

```
Terminal companion for Muxy
```

Alternatives if the primary is unavailable:

- `Control your terminal remotely` (30)
- `Remote terminal multiplexer` (27)
- `Muxy terminal companion` (23)
- `Pair, control, and ship faster` (30)

## Promotional Text

App Store Connect → Version → Promotional Text (170 char max, editable post-release without re-review).

```
Drive terminal sessions from your phone. Pair over your local network, switch projects, run commands, and review changes — all in real time.
```

## Description

App Store Connect → Version → Description.

```
Muxy Mobile is the companion app for Muxy, a terminal multiplexer for your desktop. Pair your phone over the local network and take your sessions with you.

Built for developers
Drive real terminal sessions from your phone. Switch projects, run commands, review git changes, and stay in flow when you step away from your desk.

How it works
1. Install Muxy on your desktop and enable the Mobile server in Settings.
2. Open Muxy Mobile on your phone, enter the host and port shown in Muxy.
3. Approve the pairing prompt on your desktop. You're connected.

Features
• Real-time terminal sessions over your local network
• Project and tab switching with a swipe
• Nerd Font support for powerline glyphs and icons
• Git status, branch, and diff at a glance
• Light, dark, and device-matched themes
• Demo Mode to explore the app without pairing

Privacy first
Muxy Mobile talks directly to your desktop over your local network. No cloud, no accounts, no telemetry — your terminal sessions never leave your network.

One-time purchase
Free 3-day trial on first pairing. After that, a one-time purchase unlocks the app for life on all your devices tied to your store account. No subscription.
```

## Keywords

App Store Connect → Version → Keywords (100 char max, comma-separated, no spaces).

```
terminal,multiplexer,tmux,ssh,remote,developer,coding,shell,console,muxy,companion,devtools,git
```

Do not include: `mac`, `macos`, `apple`, `iphone`, `ipad`, `xcode`, `ios`, or competitor app names.

## What's New in This Version

App Store Connect → Version → What's New (4000 char max).

```
Metadata and copy updates for clarity throughout the app.
```

## App Review Information

App Store Connect → App Review Information → Notes.

```
Muxy Mobile is the companion app for Muxy, a terminal multiplexer that runs on the reviewer's desktop computer.

Demo Mode: Since pairing requires the Muxy desktop app on the same local network, the app ships with a built-in Demo Mode that loads sample projects, sessions, and terminal output. Toggle it on from Settings → Demo → Demo Mode.

Demo video (physical iPhone + desktop hardware pairing and full workflow):
[PASTE_VIDEO_URL_HERE]

Hardware pairing flow shown in the video:
1. Muxy desktop running, Mobile server enabled.
2. Muxy Mobile on iPhone, tap Add Device.
3. Enter desktop IP and port (default 4865).
4. Approve the pairing prompt on the desktop.
5. Sessions appear on the phone and stay in sync in real time.

No login required. No account creation. No backend servers — all traffic stays on the local network.
```

Required fields:

- **Sign-in required:** No
- **Contact name / email / phone:** Saeed Vaziry contact details
- **Demo account:** Not applicable (no auth)
- **Notes:** Use the block above

## Apple Reply

Paste into the rejection thread in App Store Connect → Resolution Center.

```
Hello,

Thank you for the review.

Regarding Guideline 5.2.5 — Intellectual Property:
We have removed all references to Apple product names from the app's metadata. The subtitle now reads "Terminal companion for Muxy". The description, promotional text, and keywords have been updated to use "desktop" instead of any Apple trademark. In-app copy has been updated to match.

Regarding Guideline 2.1 — Information Needed:
A demo video showing the physical iPhone pairing and operating with the desktop hardware is linked in the App Review Information notes for this version.

A new build (0.3.1) has been uploaded with the updated metadata and copy.

Thanks,
Saeed
```

## Screenshot Audit

Before resubmit, open each screenshot and verify no text overlay reads:

- `Mac`
- `macOS`
- `for Mac`
- `from your Mac`
- Apple device imagery (Mac silhouettes, etc.)

If any are found, regenerate the screenshot with `desktop` or `your computer`.

## In-App Metadata (already updated in the repo)

These were changed in the codebase as part of the 5.2.5 fix and ship in the new binary:

- `app.json` → `NSLocalNetworkUsageDescription`
- `ios/Muxy/Info.plist` → `NSLocalNetworkUsageDescription`
- `app/onboarding.tsx`, `app/add-device.tsx`, `app/settings.tsx`, `app/projects/index.tsx`, `app/projects/[id]/index.tsx`
- `src/billing/copy.ts`
- `src/demo/demoBackend.ts` → `DEMO_DEVICE_NAME`
- `src/state/pair.ts` → pairing-denied error message
- `src/components/terminal/TerminalView.tsx` → "Desktop took control" overlay

Protocol field `{ mac: { deviceName } }` in `src/transport/protocol.ts` and `src/state/usePaneSession.ts` is intentionally untouched — it is the wire-format key shared with the Muxy desktop and is not user-visible.
