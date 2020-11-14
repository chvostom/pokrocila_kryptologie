#!/bin/bash
if [ $# -ne 2 ]; then
    echo "Příkaz: $0 [Počet plaintextů] [Klíč]"
    exit 1
fi
./random_gen.py $1 txt/ptr.bin 
./spn.py txt/ptr.bin txt/ctr.bin -k $2
echo "Count of plaintexts: $1"
echo "Key: $2"
./linear.py txt/ptr.bin txt/ctr.bin
echo "========================================================"
