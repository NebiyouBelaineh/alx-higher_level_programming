#!/usr/bin/python3
"""6-peak module to find a peak in a list"""

def find_peak(list_of_integers):
    """Finds a peak in a list of integers"""
    if list_of_integers == []:
        return None
    else:
    	 return max(list_of_integers)
