#!/usr/bin/python3
""" class Student that defines a student by :
        -first name;
        -last name;
        -age;
"""


class Student:
    """ Student init """
    def __init__(self, first_name, last_name, age):
        self.firt_name = first_name
        self.lase_name = last_name
        self.age = age

        def to_json(self):
            return self.__dict__
