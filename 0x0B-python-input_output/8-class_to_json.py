#!/usr/bin/pyhon3
"""
a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean) 
for JSON serialization of an object
"""



def class_to_json(obj):
    """ class to jason """
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
