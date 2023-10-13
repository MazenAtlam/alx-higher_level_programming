#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for ch in my_string:
        c = ord(ch)
        if c != 99 and c != 67:
            new_string += ch

    return new_string
