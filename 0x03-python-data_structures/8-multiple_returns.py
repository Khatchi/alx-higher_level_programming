#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Write a func that returns a tuple with the length of a\n
    string and its first character.
    """
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])