#!/usr/bin/env bash
# Shared helpers for scripts/release-*.sh.
# Source this file from a release script: `source "$(dirname "$0")/lib/common.sh"`

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

log() { printf "\n\033[1;36m==>\033[0m %s\n" "$*"; }
warn() { printf "\033[1;33mwarn:\033[0m %s\n" "$*" >&2; }
die() { printf "\033[1;31merror:\033[0m %s\n" "$*" >&2; exit 1; }

load_env() {
  local env_file="$REPO_ROOT/.env"
  if [[ ! -f "$env_file" ]]; then
    die ".env not found at $env_file. Copy .env.example to .env and fill in values."
  fi
  set -a
  # shellcheck disable=SC1090
  source "$env_file"
  set +a
}

require_var() {
  local name="$1"
  if [[ -z "${!name:-}" ]]; then
    die "Required env var '$name' is not set. See .env.example."
  fi
}

require_file() {
  local var_name="$1"
  require_var "$var_name"
  local path="${!var_name}"
  if [[ "$path" != /* ]]; then
    path="$REPO_ROOT/$path"
  fi
  if [[ ! -f "$path" ]]; then
    die "$var_name points to '${!var_name}' but the file does not exist (resolved to '$path')."
  fi
  printf -v "$var_name" '%s' "$path"
}

confirm() {
  local prompt="${1:-Continue?}"
  read -r -p "$prompt [y/N] " response
  [[ "$response" =~ ^[Yy]$ ]]
}

validate_version() {
  local version="$1"
  if ! [[ "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    die "Version must be in X.Y.Z format (got: $version)"
  fi
}

validate_numeric() {
  local label="$1" value="$2"
  if ! [[ "$value" =~ ^[0-9]+$ ]]; then
    die "$label must be numeric (got: $value)"
  fi
}
