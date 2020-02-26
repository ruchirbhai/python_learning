#! /usr/bin/env python3
"""
Question: Checking in a File for repeated lines and only print the repeated ones
Initial interaction without using any file operations. A very inefficient way to come up with the answer.

Improvement 1: use dictionary and go through the array only once

Assuming input is a list

File1
Input:

[Test 1,
Test 1,
Test 2,
Test 3,
Test 3,
Test 4,
Test 5,
Test 5]

Output:
Test 1
Test 3
Test 5

"""
file1 = ['Test 1',
         'Test 1',
         'Test 2',
         'Test 3',
         'Test 3',
         'Test 4',
         'Test 5',
         'Test 5',
         'Test 5',]

dict_list = {}

for file in file1:
    if file in dict_list:
        dict_list[file] += 1
    else:
        dict_list[file] = 1
#print(dict_list.items())

sort_list = [k for k, v in dict_list.items() if v >= 2]

print(sorted(sort_list))

