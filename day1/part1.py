#!/usr/bin/python3

import sys

input = sys.stdin.readlines()
total = 0
for line in input:
    first = 0
    second = 0
    for char in line:
        if char.isnumeric() and first == 0:
            first = char
    for char in line[::-1]:
        if char.isnumeric() and second == 0:
            second = char

    total += int(first + second)

print(total)
