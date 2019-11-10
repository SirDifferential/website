#!/bin/bash

FILES=`find . -name '*.md'`
for f in $FILES
do
    echo "Converting $f"
    bash build.sh $f
done

bash create_list.sh
