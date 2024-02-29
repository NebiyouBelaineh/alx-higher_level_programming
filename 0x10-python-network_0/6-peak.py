#!/usr/bin/python3
"""6-peak module to find a peak in a list"""

def find_peak(list_of_integers):
    """Finds a peak in a list of integers"""
    if list_of_integers == [] or list_of_integers is None:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]  # return only element inside list
    if len (list_of_integers) == 2:
        return max(list_of_integers)  # compare two digits and return max
    # Three elements and above lists
    max_index = len(list_of_integers)
    mid_index = int((max_index) / 2)
    if list_of_integers[mid_index] >= list_of_integers[mid_index - 1]\
        and list_of_integers[mid_index] >= list_of_integers[mid_index + 1]:
            return list_of_integers[mid_index]
    if mid_index > 0 and list_of_integers[mid_index] < list_of_integers[mid_index + 1]:
        return find_peak(list_of_integers[mid_index:])
    if mid_index > 0 and list_of_integers[mid_index] < list_of_integers[mid_index - 1]:
        return find_peak(list_of_integers[:mid_index])
    
