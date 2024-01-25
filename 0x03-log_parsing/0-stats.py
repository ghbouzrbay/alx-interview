#!/usr/bin/env python3
"""script that reads stdin line by line and computes metrics
"""

import re

def parse_log_line(line):
    '''Extracts sections of a line of an HTTP request log.
    '''
    pattern = r'^(?P<ip>\S+) - \[(?P<date>\d{2}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{1,3})\] "GET (?P<request>[^ ]+) HTTP/1\.\d+" (?P<status_code>\d+) (?P<file_size>\d+)$'
    match = re.match(pattern, line)
    if match:
        return match.groupdict()
    else:
        return {}

def print_stats(total_file_size, status_codes):
    '''Prints the accumulated statistics of the HTTP request log.
    '''
    print('Total file size: {:d}'.format(total_file_size))
    for status_code in sorted(status_codes.keys()):
        num = status_codes.get(status_code, 0)
        if num > 0:
            print('{}: {}'.format(status_code, num))

def update_metrics(line, total_file_size, status_codes):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    '''
    parsed_line = parse_log_line(line)
    if parsed_line:
        status_code = parsed_line['status_code']
        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1
        total_file_size += int(parsed_line['file_size'])
    return total_file_size

def main():
    '''Starts the log parser.
    '''
    total_file_size = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(line, total_file_size, status_codes)
            if line and line[-1] != '\n':
                line += input()
            if line:
                print_stats(total_file_size, status_codes)
    except (KeyboardInterrupt, EOFError):
        print_stats(total_file_size, status_codes)

if __name__ == '__main__':
    main()
