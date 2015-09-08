#!/usr/bin/env python3
"""
This script parses a MIPS kernel panic and converts machine code back
to assembly instructions.
"""
import subprocess
import sys
import os

SCRIPT = os.path.join(os.getcwd(), 'convert.sh')

def main():
    if len(sys.argv) < 2:
        print('{0} <kernel panic file>'.format(sys.argv[0]))
        exit()

    with open(sys.argv[1], 'r') as f:
        for line_cnt, line in enumerate(f):
            if 'Code:' in line and 'Bad' not in line:
                line = line.split('Code: ')[1]
                print('Line: {0}\n{1}'.format(line_cnt, line), end='')
                print_code(line.split())
                print()

def print_code(codes):
    for c in codes:
        print(subprocess.check_output([SCRIPT, c.strip('<>')]).decode('utf-8'), end='')

if __name__ == '__main__':
    main()
