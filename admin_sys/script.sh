#!/bin/bash

ma_liste=("Master" "Informatique" "Développement" "DATA")

for i in "${ma_liste[@]}"; do
    echo "l'élément $i est dans la liste"
done