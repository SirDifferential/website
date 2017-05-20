#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: build.sh input.md output.html"
    exit 1
fi

SRCFILE=$1
if [ ! -f $SRCFILE ]; then
    echo "No such file: $SRCFILE"
    exit 1
fi

OUTFILE=$2

markdown $SRCFILE > temp.html
sed -i 's/<code>/<pre>/g' temp.html && sed -i 's/<\/code>/<\/pre>/g' temp.html
sed -e '/<blogtext>/ {r temp.html
d}' base.html > $OUTFILE
