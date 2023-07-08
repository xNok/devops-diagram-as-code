#!/bin/bash
# activate glob ignore
shopt -s extglob

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
echo "Executed from ${parent_path}"

FOLDERS=(excalidraw plantuml)

for FOLDER in ${FOLDERS[@]}; do
  for f in $FOLDER/**/*
    do 
        if [ "${f: -3}" == "svg" ]; then
            continue 
        fi
        echo "Generate $f"
        INPUT=$f
        TYPE=$FOLDER
        ./kroki convert $INPUT --type $TYPE
    done 
done



