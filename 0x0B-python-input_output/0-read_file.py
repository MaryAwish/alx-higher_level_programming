#!/usr/bin/python3
"""
Module contains a function that reads from a file
"""


def read_file(filename=""):
    """Function that reads from a file

    Args:
        filename: filename

    Raises
        Exceptions: when the file can be opened

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
