#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        c = ord(ch)
        if c >= 97 and c <= 122:
            ch = chr(c - 32)
        print("{}".format(ch), end='')
    print()
