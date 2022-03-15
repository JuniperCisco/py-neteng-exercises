# -*- coding: utf-8 -*-
"""
Task 7.3b

Make a copy of the code from the task 7.3a.

Add this functionality:
- Ask the user to enter the VLAN number.
- Print information only for the specified VLAN.

Output example:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
mac_table = []
vlan_number = input("Please, enter VLAN number: ")

with open("CAM_table.txt") as conf:
    for line in conf:
        words = line.split()
        if words and words[0].isdigit() and words[0] == vlan_number:
            vlan, mac, _, intf = words
            mac_table.append([int(vlan), mac, intf])


for vlan, mac, interface in sorted(mac_table):
    print(f"{vlan:<9}{mac:20}{intf}")



