#!/usr/bin/python3
"""
A script: Reads standard input line by line and compute stats
"""


def parseList():
    """
    Parses a single line of log and extracts IP address, status code, and file size.

    Args:
        line (str): Single line of log entry.

    Returns:
        tuple: Tuple containing IP address (str) and tuple of status code (str) and file size (int).
    """
    stdin = __import__('sys').stdin
    lineNumber = 0
    fileSize = 0
    statusCodes = {}
    codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    try:
        for line in stdin:
            lineNumber += 1
            line = line.split()
            try:
                fileSize += int(line[-1])
                if line[-2] in codes:
                    try:
                        statusCodes[line[-2]] += 1
                    except KeyError:
                        statusCodes[line[-2]] = 1
            except (IndexError, ValueError):
                pass
            if lineNumber == 10:
                printReport(fileSize, statusCodes)
                lineNumber = 0
        printReport(fileSize, statusCodes)
    except KeyboardInterrupt as e:
        printReport(fileSize, statusCodes)
        raise


def printReport(fileSize, statusCodes):
    """
    Prints generated report to standard output
    Args:
        fileSize (int): total log size after every 10 lines read
        statusCodes (dict): dict of status codes and counts
    """
    print("File size: {}".format(fileSize))
    for key, value in sorted(statusCodes.items()):
        print("{}: {}".format(key, value))


if __name__ == '__main__':
    parseList()
