#!/bin/bash

FILES=`find . -name '*.md'`
for f in $FILES
do
    echo "Converting $f"
    sh build.sh $f
done

