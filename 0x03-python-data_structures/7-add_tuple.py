#!/usr/bin/python3
def assign_terms(tuple_x, len_x):
    if len_x == 0:
        return 0, 0
    elif len_x == 1:
        return int(tuple_x[0]), 0
    else:
        return int(tuple_x[0]), int(tuple_x[1])


def add_tuple(tuple_a=(), tuple_b=()):
    a1, a2 = assign_terms(tuple_a, len(tuple_a))
    b1, b2 = assign_terms(tuple_b, len(tuple_b))
    sum = (a1 + b1, a2 + b2)
    return sum
