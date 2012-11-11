#!/usr/bin/env python
# encoding: utf=8

import os
from abjad import *
path = os.path.realpath(__file__)
f = open(path, 'r')
staff = Staff();
for line in f:
    for char in line:
        if char == 'a' or char == 'A':
            staff.append(Note(0, (1,8)))
        elif char == 'e' or char == 'E':
            staff.append(Note(2, (1,8)))
        elif char == 'i' or char == 'I':
            staff.append(Note(4, (1,8)))
        elif char == 'o' or char == 'O':
            staff.append(Note(7, (1,8)))
        elif char == 'u' or char == 'O':
            staff.append(Note(9, (1,8)))
        elif char == 'y' or char == 'Y':
            staff.append(Note(10, (1,8)))
        else:
            staff.append(Rest((1,8)))
f.close()
show(staff)

