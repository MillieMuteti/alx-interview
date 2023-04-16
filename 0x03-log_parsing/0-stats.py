#!/usr/bin/python3
'''script reading stdin line by line and computing metrics'''


import sys

status = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
summation = 0
tmp = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in status.keys():
                status[code] += 1
            summation += size
            tmp += 1

        if tmp == 10:
            tmp = 0
            print('File size: {}'.format(summation))
            for key, value in sorted(status.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(summation))
    for key, value in sorted(status.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
