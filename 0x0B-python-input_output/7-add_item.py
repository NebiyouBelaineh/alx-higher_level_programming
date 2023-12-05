#!/usr/bin/python3
"""This script adds all arguments to a Python list,
and then saves them to a file: add_item.json"""
import os
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """Adds the argument to <json_list> everytime it is called"""

    args = sys.argv
    filename = 'add_item.json'

    if not os.path.isfile(filename):
        save_to_json_file([], filename)
        return
    loaded_obj = load_from_json_file(filename)
    for i in range(1, len(args)):
        # open file and get list from json file
        # convert list to python object using load_from_json_file()
        # append if i not a list, otherwise extend it
        # use save_to_json_file() to save object to file
        loaded_obj.append(args[i])
        save_to_json_file(loaded_obj, filename)


add_item()
