#!/bin/sh -e

git add .
git diff --staged
git status
msg="$(date +%Y/%d)"
printf "commit message [default=%s]: " "$msg"
read -r ans
if [ "$ans" ]; then msg="$ans"; fi
git commit -m "$msg"
git push
