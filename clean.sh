#!/bin/bash
# Written by Kevin Cole <kevin.cole@novawebdevelopment.org> 2017.07.01
#
# Find all HTML files with unprintable stuff
#

for i in $(find . -iname "*.htm*")
do
  perl -p -i -e "s|\r\n|\n|g;" $i
done

for i in $(find . -iname "*.htm*")
do
  grep -H --color="auto" -P -n "[^\x00-\x7E]" $i
  read -p "Continue? "
  grep -H --color="auto" -P -n "[\x00-\x1E]"  $i
  read -p "Continue? "
done
