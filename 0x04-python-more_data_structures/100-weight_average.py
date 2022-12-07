#!/usr/bin/python3
def weight_average(my_list=[]):
    avg = 0
    sum_weight = 0
    sum_score = 0
    if (len(my_list) <= 0):
        return (0)
    for item in my_list:
        score, weight = item
        sum_weight += weight
        sum_score += score * weight
    return sum_score / sum_weight
