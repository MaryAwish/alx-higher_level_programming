#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    i = len(my_list)
    copy_lst = my_list.copy()

    if idx < 0:
        return copy_lst
    elif idx > i - 1:
        return copy_lst
    else:
        copy_lst[idx] = element
        return copy_lst
