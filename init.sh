#!/bin/sh -e

cd "$(dirname "$0")"

cookie="$(cat cookie)"

year="$1"
day="$2"

[ "$day" ]  || day="$(date +%d)"
[ "$year" ] || year="$(date +%Y)"

day="$(printf '%d' "$day")"
day02="$(printf '%02d' "$day")"
mkdir -p "$year/$day02"
cd "$year/$day02"

echo "https://adventofcode.com/$year/day/$day"
[ -s input ] || curl -s -b "session=$cookie" "https://adventofcode.com/$year/day/$day/input" > input
curl -s -b "session=$cookie" "https://adventofcode.com/$year/day/$day" > page.html
touch "$day02.py" sample1.txt
html2text page.html > page.txt
