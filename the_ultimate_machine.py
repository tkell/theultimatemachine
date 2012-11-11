#!/usr/bin/env python
# encoding: utf=8

# Welcome to the_ultimate_machine.py
# the_ultimate_machine.py is a deeply meta music creation script / framework.
# It runs its OWN TEXT through the algorithm that it defines.  
# To use the_ultimate_machine.py, simple replace the below parsing code with code of your own
# Note that to run the_ultimate_machine.py properly, you should remove ALL comments, 
# except for the shabang and encoding, and compact the code as much as possible.  
# This version uses abjad and lilypond to create scores.  
# You may use any midi, audio, or score-creation libraries, so long as the script only points to itself.

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

