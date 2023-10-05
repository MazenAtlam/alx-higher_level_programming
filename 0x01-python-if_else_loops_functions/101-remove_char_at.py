#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    str_copy = ''
    i = 0
    for ch in str:
        if i == n:
            i += 1
            continue
        str_copy += ch
        i += 1
    return str_copy
