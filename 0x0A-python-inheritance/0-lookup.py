#!/usr/bin/python3
"""Contains lookup function
"""


def lookup(obj):
    """returns a list of available attributes of an object"""
    return dir(obj)
