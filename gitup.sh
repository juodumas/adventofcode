#!/bin/sh -e

git add .
git diff --staged
git status
printf "commit & push? [yN] "
read ans
if [ $ans = y ] || [ $ans = Y ]; then
    git commit -m up
    git push
fi
