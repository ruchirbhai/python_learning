#! /usr/bin/env python3
"""
Question: Checking in a File for repeated lines and only print the repeated ones
Initial interaction without using any file operations. A very inefficient way to come up with the answer.

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
         'Test 5']

final_list = set()

for file in file1:
    count = 0
    for value in file1:
        if value == file:
            count += 1
            #print(value)
        if count == 2:
            #print(value)
            break

    if count == 2:
        final_list.add(file)
        #print("here")

print(sorted(final_list))

