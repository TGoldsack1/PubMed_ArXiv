#!/bin/bash
# Author: Tomas Goldsack

fileid="1b3rmCSIoh6VhD4HKWjI4HOW-cSwcwbeC"
filename="arxiv-data.zip"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}


fileid="1lvsqvsFi3W-pE1SqNZI0s8NR9rC1tsja"
filename="pubmed-data.zip"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}