#!/usr/bin/python3
def roman_value(character):
    roman_list = [('I', 1), ('V', 5), ('X', 10),
                  ('L', 50), ('C', 100), ('D', 500), ('M', 1000)]
    for item in roman_list:
        key, value = item
        if character is key:
            return value
    return None


def next_value(String, Index):
    if Index + 1 < len(String):
        return roman_value(String[Index + 1])
    else:
        return None


def roman_to_int(roman_string):
    result = 0

    if (roman_string is None or isinstance(roman_string, str) is False):
        return result

    enum = enumerate(roman_string)
    for key, value in enum:
        curr_value = roman_value(value)
        next_val = next_value(roman_string, key)
        if next_val is None or curr_value >= next_val:
            result += curr_value
        else:
            result += (next_val - curr_value)
            next(enum)
    return result
