#!/usr/bin/bash

printf "$(git diff --name-only HEAD~1)" > del.txt

filename="commands.txt"

python extract1.py

while read -r line
do
	$line

done < $filename

rm -f "del.txt"
rm -f "commands.txt"
