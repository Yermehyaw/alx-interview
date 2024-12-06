#!/usr/bin/python3
"""
Parse a log file from stdin, prints the parsed output for every 10th line
received or on receiving a SIGINT(Ctrl+C) signal

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

signal_received = False  # flag to prevent reentrant code


def handler(sig: int, frm: Optional[FrameType]) -> None:
    """Handles Ctrl + C signals"""
    global signal_received
    signal_received = True


# register handler to the SUGINT signal
signal.signal(signal.SIGINT, handler)  # handle ctrl+c signals

try:
    n = 0

    for line in sys.stdin:
        n += 1
        line_list = line.split()
        print(line_list)

        try:
            len_line = len(line_list)
            if len_line == 9:
                size = int(line_list[8])
                code = int(line_list[7])
            elif len_line == 8:
                size = int(line_list[7])
                code = int(line_list[6])

        except (IndexError, ValueError, NameError):
            code = None
            size = 0

        total_size += size
        if code:
            try:
                stat_codes[str(code)] += 1
            except (KeyError):
                pass

        if n % 10 == 0:  # 10th-ish iteration e.g 10, 20, 30 etc
            print(f'File size: {total_size}')
            for stat, code in stat_codes.items():
                if code > 0:  # if code is greater than 0
                    print(f'{stat}: {code}')

        if signal_received:
            break

    print(f'File size: {total_size}')
    for stat, code in stat_codes.items():
        if code > 0:
            print(f'{stat}: {code}')

except (BrokenPipeError, IOError, EOFError) as e:
    sys.exit(1)
