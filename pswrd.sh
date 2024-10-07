#!/bin/bash

SAVE_PATH="./.credentials"

REF="$1"

PSWRD=""

if [ $# -eq 0 ]; then
	echo "you need to provide a login to be associated with the password"
	exit 1
else
	PSWRD=$(apg -m 14 -x 18 -n 1)
	echo "password selected for $REF is: $PSWRD"

	while true; do

		read -p "save it, generate another one or leave? (Y/g/n): " choice

		case $choice in
			[Yy]*)
				echo -e "$REF=$PSWRD\n" >> $SAVE_PATH
				echo "password saved in $SAVE_PATH"
				exit 0
				;;
			[Gg]*)
				PSWRD=$(apg -m 14 -x 18 -n 1)
				echo -e "\npassword selected for $REF is: $PSWRD" 
				continue
				;;
			[Nn]*)
				echo -e "\n[exiting...]"
				exit 0
				;;
			*)
				echo -e "\n[invalid choice]"
				;;
		esac
	done
fi


