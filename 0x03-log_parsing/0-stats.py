#!/usr/bin/python3
'''script that reads stdin line by line and computes metrics'''
import re


def extract(linput):
    '''Extracts sections of a line of an HTTP request log.'''
    file_p = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    id_info = {
        'status_code': 0,
        'file_size': 0,
    }
    log = '{}\\-{}{}{}{}\\s*'.format(file_p[0], file_p[1], file_p[2], file_p[3], file_p[4])
    resp = re.fullmatch(log, linput)
    if resp is not None:
        code = resp.group('code')
        size = int(resp.group('size'))
        id_info['code'] = code
        id_info['size'] = size
    return id_info


def statistic(size, stats):
    '''Prints the accumulated statistics of the HTTP request log.'''
    print('File size: {:d}'.format(size), flush=True)
    for code in sorted(stats.keys()):
        num = stats.get(code, 0)
        if n > 0:
            print('{:s}: {:d}'.format(code, n), flush=True)


def update(line, size, stats):
    '''Updates the metrics from a given HTTP request log.'''
    id_info = linput(line)
    code = id_info.get('code', '0')
    if code in stats.keys():
        stats[code] += 1
    return size + id_info['size']


def startrun():
    '''Starts the log parser.'''
    lline = 0
    size = 0
    stats = {
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
            size = update(
                line,
                size,
                stats,
            )
            lline += 1
            if lline % 10 == 0:
                statistics(size, stats)
    except (KeyboardInterrupt, EOFError):
        statistics(size, stats)


if __name__ == '__main__':
    startrun()
