# -*- coding: utf-8 -*-
"""
Task 7.3

The script should process the lines in the CAM_table.txt file. Each line,
where there is a MAC address, must be handled in such a way that
the following table was printed on the stdout:

100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
300      a2ab.c5a0.700e      Gi0/3
10       0a1b.1c80.7000      Gi0/4
500      02b1.3c80.7b00      Gi0/5
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
10       01ab.c5d0.70d0      Gi0/8
1000     0a4b.c380.7d00      Gi0/9


Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

'''
@natenka solution
'''
with open("CAM_table.txt") as conf:
    for line in conf:
        words = line.split()
        if words and words[0].isdigit():
            vlan, mac, _, interface = words
            print(f"{vlan:9}{mac:20}{interface}")

'''
My own solution:


with open('CAM_table.txt') as f:
    for line in f:
        if '.' in line:
            print(line.replace('DYNAMIC', '').rstrip())
'''