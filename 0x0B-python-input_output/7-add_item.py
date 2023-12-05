#!/usr/bin/python3
"""This script adds all arguments to a Python list,
and then saves them to a file: add_item.json"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# use save_to... for saving to file
# use load_from ... to load and then append and save again using save_to


def add_item(filename, args=[]):
    import os
    """Adds the argument to <json_list> everytime it is called"""
    if not os.path.isfile(filename):
        save_to_json_file([], filename)
        return
    loaded_obj = load_from_json_file(filename)
    for i in range(1, len(args)):
        # open file and get list from json file
        # convert list to python object using load_from_json_file()
        # append if i not a list, otherwise extend it
        # use save_to_json_file() to save object to file
        if type(args[i]) is not list:
            loaded_obj.append(args[i])
        else:
            loaded_obj.extend(args[i])
    save_to_json_file(loaded_obj, filename)


def main():
    """Main entry point of the program"""
    import json
    import sys

    args = sys.argv
    filename = 'add_item.json'
    add_item(filename, args)


main()
