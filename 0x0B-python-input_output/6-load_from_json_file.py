#!/usr/bin/python3
"""This module defines a function that  creates an Object from a
“JSON file”"""
import json


def load_from_json_file(filename):
    """Creates an Object from JSON File"""
    with open(filename, 'r', encoding='utf-8') as json_file:
        obj = json.load(json_file)
        return obj
