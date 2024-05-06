#!/usr/bin/python3

import sys
from collections import defaultdict

def print_stat(total_size, status_counts):
    """
    Prints statistics based on total file size and status code counts.

    Args:
        total_size (int): Total file size.
        status_counts (dict): Dictionary containing counts of status codes.

    Returns:
        None
    """
    print("Total file size:", total_size)
    for code, count in sorted(status_counts.items()):
        print(f"{code}: {count}")

def parseLne(line):
    """
    Parses a single line of log and extracts IP address, status code, and file size.

    Args:
        line (str): Single line of log entry.

    Returns:
        tuple: Tuple containing IP address (str) and tuple of status code (str) and file size (int).
    """
    parts = line.split()
    if len(parts) != 10:
        return None, None
    ip_address = parts[0]
    status_code = parts[-2]
    file_size = int(parts[-1])
    return ip_address, (status_code, file_size)

def main():
    """
    Main function to read logs from standard input and generate reports.
    """
    total_size = 0
    status_counts = defaultdict(int)
    try:
        for i, line in enumerate(sys.stdin, start=1):
            ip_address, data = parseLne(line.strip())
            if data is None:
                continue
            status_code, file_size = data
            total_size += file_size
            status_counts[status_code] += 1

            if i % 10 == 0:
                print_stat(total_size, status_counts)
    except KeyboardInterrupt:
        # Handle KeyboardInterrupt and print final statistics
        print_stat(total_size, status_counts)

if __name__ == "__main__":
    main()
