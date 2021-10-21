#!/bin/bash

sh build.sh index.md

# Get all blog_*.html files
BLOGS=`find . -name 'blog_*' |grep '\.html$'`

if [ -f bloglist.md ]; then
    rm bloglist.md
fi

touch bloglist.md

for b in $BLOGS
do
    # extract date from datetag
    DATE=`cat $b |grep '<datetag=' | sed 's/.*=//' |sed 's/>.*//'`

    # extract headline from the original .md file
    MDFILE=`echo $b |sed 's/.html/.md/g'`
    HEADLINE=`head -1 $MDFILE |sed 's/#//g'`

    echo $b $DATE $HEADLINE
    # Write a markdown link in the blog list
    echo "* $DATE [$HEADLINE]($b)" >> bloglist.md
done

python3 sort_entries.py bloglist.md
RETCODE=$?
if [ $RETCODE != 0 ]; then
    echo "Failed sorting entries"
    exit 1
fi

python3 ./create_rss.py ./bloglist.md ./rss.xml

# Convert the generated markdown into html
pandoc -f markdown -t html bloglist.md > bloglist.html

mv index.html temp.html

# replace the generated bloglist html into the index html page bloglist tag
sed -e '/<bloglist>/ {r bloglist.html
d}' temp.html > index.html
rm temp.html

