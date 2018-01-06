#!/bin/bash

while read item; do
	echo ""
	python ge_api.py $item
done <items.txt

echo ""
#python ge_api.py 1937
