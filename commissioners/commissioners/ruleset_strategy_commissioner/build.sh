#!/usr/bin/env sh
set -eu

repo_root="$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)"
"$repo_root/commissioners/build_image.sh" config_driven ghcr.io/softmax-universe/commissioners-default:latest default
