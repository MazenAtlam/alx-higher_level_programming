#!/usr/bin/python3
def search_replace(my_list, search, replace):
    idx = my_list.index(search)
    my_list.remove(search)
    my_list.insert(idx, replace)
    return my_list
