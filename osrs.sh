#!/bin/bash

if [ -z "$1" ] 
then
	figlet RUNESCAPE
	java -jar ~/Downloads/osbuddy/OSBuddy.jar > /dev/null
else
	figlet ALTSCAPE
	for (( i=0; i<$1; i++ )) 
	do
		java -jar ~/Downloads/osbuddy/OSBuddy.jar > /dev/null
	done
fi

