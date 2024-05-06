#!/usr/bin/python3
"""log parsing"""
import sys
import re
import signal


def signal_handler(sig, frame):
    """handling the ctrl +c signal"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

line_count = 0
file_size = 0
status_codes = {}

for line in sys.stdin:
    line_count += 1

    # Use regular expressions to extract data
    match = re.search(
        r'^(\S+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$', line)
    if not match:
        continue

    status_code = int(match.group(2))
    size = int(match.group(3))

    # Update file size and status code counts
    file_size += size
    status_codes[status_code] = status_codes.get(status_code, 0) + 1

    # Print statistics every 10 lines read
    if line_count % 10 == 0:
        print_stats()

    def print_stats():
        """Prints the statistics to the standard output"""
        print("File size:", file_size)
        for code in sorted(status_codes):
            print("{}: {}".format(code, status_codes[code]))

