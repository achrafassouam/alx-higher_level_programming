#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    for value in my_list:
        return list(map(lambda value: value * number, my_list))
