#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_weight = 0
    sum_score = 0
    for project in my_list:
        sum_weight += project[1]
        sum_score += project[0] * project[1]

    return (sum_score / sum_weight)
