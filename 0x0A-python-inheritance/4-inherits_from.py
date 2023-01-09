#!/usr/bin/pyhton3
"""
Contains function inherits_from
"""


def inherits_from(obj, a_class):
    """returns true if the obj is a subclass of _a_class, else false"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
