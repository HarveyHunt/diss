#!/bin/bash
if [ $# -ne 1 ]; then
    echo $(basename "$0") "<hex code>"
    exit 1
fi

if [[ $1 == "0x"* ]]; then
    code=$1
else
    code="0x$1"
fi

cat >$code.S <<EOL
.text
sym:    .word $code
EOL

mipsel-linux-gnu-gcc -c -o $code.o $code.S
mipsel-linux-gnu-objdump -b binary -D -s -EL -mmips:isa32 $code.o \
    -Mgpr-names=32mcp0-names=mips32,hwr-names=mips32,reg-names=mips32 |\
    grep ${1#"0x"} |\
    tail -n 1 |\
    cut -f 2-
rm $code.o
rm $code.S
