#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqList_set = set(my_list)
    sum = 0
    for n in uniqList_set:
        sum += n

    return sum
