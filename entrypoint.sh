#!/bin/sh
set -e

pip install --no-cache-dir -r requirements.txt

exec "$@"
