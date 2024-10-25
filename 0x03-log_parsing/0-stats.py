#!/usr/bin/python3
"""
Parse a log file from stdin
Modules Imported: sys
sys: access computer resources from python
signal: handle signals
typing: various type annotations in py

"""
import sys
import signal
from types import FrameType
from typing import List
from typing import Optional


def handler(sig: int, frm: Optional[FrameType]) -> None:
    """Handles Ctrl + C signals"""
    print(f'File size: {total_size}')
    for stat, code in stat_codes.items():
        if code > 0:
            print(f'{stat}: {code}')
    sys.exit(0)


signal.signal(signal.SIGINT, handler)  # hadle ctrl+c signals

try:
    n = 0
    stat_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
    total_size = 0

    for line in sys.stdin:
        n += 1
        line_list = line.split()

        len_line = len(line_list)
        if len_line == 9:
            size = int(line_list[8])
            code = line_list[7]
        elif len_line == 8:
            size = int(line_list[7])
            code = line_list[6]

        try:
            code = int(code)
        except (ValueError, NameError):
            code = None

        total_size += size
        if code:
            stat_codes[str(code)] = stat_codes.get(str(code)) + 1

        if n % 10 == 0:  # 10th-ish iteration e.g 10, 20, 30 etc
            print(f'File size: {total_size}')
            for stat, code in stat_codes.items():
                if code > 0:  # if code is greater than 0
                    print(f'{stat}: {code}')

except (KeyboardInterrupt, BrokenPipeError, IOError, EOFError) as e:
    handler(None, None)
