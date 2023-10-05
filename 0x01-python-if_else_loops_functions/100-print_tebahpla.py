#!/usr/bin/python3
lower_turn = True
for ch in range(122, 96, -1):
    if lower_turn:
        print("{:c}".format(ch), end='')
        lower_turn = False
    else:
        print("{:c}".format(ch - 32), end='')
        lower_turn = True
