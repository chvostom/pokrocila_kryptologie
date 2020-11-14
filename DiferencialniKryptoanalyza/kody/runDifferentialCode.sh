#!/bin/bash
if [ $# -ne 2 ]; then
    echo "Příkaz: $0 [Počet plaintextů] [Klíč]"
    exit 1
fi
cp differential.py differentialNEW.py
sed -i "s/size = 10000/size = $1/g" differentialNEW.py
sed -i "s/enc_key = 0x3b6c/enc_key = $2/g" differentialNEW.py
echo "Nastavený počet plaintextů: $1"
echo "Nastavený klíč: $2"
./differentialNEW.py
echo "========================================================"
rm differentialNEW.py
