#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght > 0:
        new = (lenght, sentence[0])
    else:
        new = (lenght, None)
    return new
