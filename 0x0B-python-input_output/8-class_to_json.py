#!/usr/bin/pyhon3
"""
a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean) 
for JSON serialization of an object
"""



def class_to_json(obj):
    """ class to jason """
    return obj.__dict__
