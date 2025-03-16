#!/usr/bin/python3
"""
Script to read stdin line by line and compute metrics.
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Prints statistics every 10 lines and on keyboard interruption.
"""

import sys
import signal

# Initialize metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """
    Print the computed statistics.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """
    Handle keyboard interruption (CTRL + C).
    """
    print_stats()
    sys.exit(0)


# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)


try:
    for line in sys.stdin:
        # Parse the line
        parts = line.split()
        if len(parts) < 7:
            continue

        # Extract file size and status code
        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
        except (ValueError, IndexError):
            continue

        # Update metrics
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except Exception:
    pass

finally:
    # Print stats at the end (e.g., for empty files or keyboard interruption)
    print_stats()
