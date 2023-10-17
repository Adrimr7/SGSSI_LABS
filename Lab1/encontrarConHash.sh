#!/bin/bash


while getopts "c:h:" opt; do #opciones
  case $opt in
    c) carp="$OPTARG";;
    h) hash="$OPTARG";;
    \?)
        echo "Error -> $0 -c <carpeta> -h <hash>"
        exit 1;;
  esac
done


if [ -z "$carp" ] || [ -z "$hash" ]; then
     echo "Error -> $0 -c <carpeta> -h <hash>"
     exit 1
fi
enc=false
for archivo in "$carp"/*; do
    hash_archivo=$(md5sum "$archivo" | awk '{print $1}')
    
    if [ "$hash_archivo" == "$hash" ]; then
        echo "Archivo encontrado: $archivo con el hash $hash"
        enc=true
        break
fi
done
if [ "$enc" == "false" ]; then
    echo "El hash $hash no está entre estos archivos." 
fi
