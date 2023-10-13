#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    first_loop = True
    for key in a_dictionary:
        if first_loop:
            key_max = key
            max = a_dictionary[key]
            first_loop = False
        if a_dictionary[key] > max:
            key_max = key
            max = a_dictionary[key]
    return key_max
