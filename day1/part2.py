#!/usr/bin/python3

import sys

input = sys.stdin.readlines()
numbers = {"one": "1", "two": "2", "three":"3", "four":"4", "five": "5",
           "six": "6", "seven": "7", "eight": "8", "nine": "9"}
total = 0

for line in input:
    one = 0
    two = 0
    for i in range(len(line)):
        if line[i].isnumeric():
            one = line[i]
            break
        for j in numbers.keys():
            if j in line[:i + 1]:
                one = numbers[j]
                break
        else:
            continue
        break

    for i in range(len(line) - 1, -1, -1):
        if line[i].isnumeric():
            two = line[i]
            break
        for j in numbers.keys():
            if j in line[i:]:
                two = numbers[j]
                break
        else:
            continue
        break
    total += int(one + two)

print(total)
