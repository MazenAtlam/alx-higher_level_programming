#!/usr/bin/python3
def islower(c):
    ch = ord(c)
    for i in range(97, 123):
        if ch == i:
            return True
    else:
        return False
