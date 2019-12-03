# !/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
import os
import sys


def print_files():
    if len(sys.argv) <= 1:
        print('Usage:', sys.argv[0], '<dir path>')
        return

    dir_ = sys.argv[1]

    output = ''
    name = '.*\..*'
    arr = []
    for f in os.listdir(dir_):
        if (os.path.isfile(f)) and (re.search(name, f)):
            size = os.path.getsize(f)
            n = re.search(name, f).group(0)
            arr.append([n, size])
    for i in range(len(arr) - 1):
        if arr[i][1] < arr[i + 1][1]:
            a = arr[i][1]
            b = arr[i + 1][1]
            arr[i][1] = b
            arr[i + 1][1] = a
    for i in arr:
        output = output + i[0] + '  ' + str(i[1]) + '\n'
    output = output[0:len(output) - 1]

    return output


if __name__ == "__main__":
    print_files()
