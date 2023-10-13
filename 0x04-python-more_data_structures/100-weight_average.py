#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0

    sum_weight = 0
    sum_score = 0
    for project in my_list:
        sum_weight += project[1]
        sum_score += project[0] * project[1]

    return (float(sum_score) / float(sum_weight))
