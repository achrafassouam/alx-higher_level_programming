#!/usr/bin/pyhon3
""" d """


def class_to_json(obj):
    """ d """
    return_dict = {}
    if hasattr(obj, "__dict__"):
        for key, value in obj.__dict__.items():
            if type(value) in [list, dict, str, int, bool]:
                return_dict[key] = value
            elif type(value) is dict:
                return_dict[key] = dict(value)
            elif type(value) is list:
                return_dict[key] = list(value)
        return return_dict
