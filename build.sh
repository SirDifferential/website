#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: sh build.sh input.md"
    exit 1
fi

SRCFILE=$1
if [ ! -f $SRCFILE ]; then
    echo "No such file: $SRCFILE"
    exit 1
fi

# Output filename is the input filename, but with html
OUTFILE=`echo $1 |sed 's/.md/.html/g'`

# See if hard-coded date is used
DATETAG=`grep -i '<datetag=' $SRCFILE`
DATETAG_LINES=`grep -i '<datetag=' $SRCFILE | wc -l`

# convert markdown into hmtl
pandoc -f markdown -t html $SRCFILE > temp.html

# copy the base html page and replace the blog contents tag with the newly generated html
sed -e '/<blogtext>/ {r temp.html
d}' base.html > $OUTFILE

if [ $DATETAG_LINES -gt 0 ]; then
    # Extract the date
    DATESTR=`echo $DATETAG | sed 's/datetag=//g' | sed 's/<//g' | sed 's/>//g'`

    # Create a date tag to be used in page listing and create a date subtitle
    sed -i 's/<datetag>//g' $OUTFILE
    sed -i "s/<datetag=.*>/$DATETAG\n<p class=\"datesubtitle\">$DATESTR<\/p>/g" $OUTFILE
else
    # Append current date in the date tag
    sed -i "s/<datetag>/<datetag=`date -I`>/g" $OUTFILE
fi

rm temp.html

