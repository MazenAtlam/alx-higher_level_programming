#!/usr/bin/python3
def search_replace(my_list, search, replace):
    obj_list = list(map(lambda ob: replace if ob == search else ob, my_list))
    return obj_list
