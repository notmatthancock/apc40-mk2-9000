#!/usr/bin/env bash

NAME=APC40_MkII_9000
SCRIPTS_FOLDER="Contents/App-Resources/MIDI Remote Scripts"

if [[ -z "$ABLETON_FOLDER" ]]; then
  ABLETON_FOLDER=$(ls -1t /Applications | grep "Ableton Live 11" | head -n 1 | tr -d '\n')
fi

PREFIX=/Applications/$ABLETON_FOLDER
if [ ! -d "$PREFIX" ]; then
  echo Ableton folder \"$PREFIX\" does not exist. Exiting.
  exit 1
fi

FULL_PATH=$PREFIX/$SCRIPTS_FOLDER/$NAME
while true; do
    echo will install to \"$FULL_PATH\"
    read -p "Continue? [y/n] " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) echo K bye; exit;;
        * ) echo "Please answer y/n";;
    esac
done

cp -r ./$NAME "$FULL_PATH"
