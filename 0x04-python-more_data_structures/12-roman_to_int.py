#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)

    rome_nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    dec_num = 0

    for i in range(len(roman_string)):
        if rome_nums.get(roman_string[i], 0) == 0:
            return (0)
        if i != (len(roman_string) - 1) and rome_nums[roman_string[i]] < rome_nums[roman_string[i + 1]]:
                dec_num += rome_nums[roman_string[i]] * -1
        else:
            dec_num += rome_nums[roman_string[i]]
    return (dec_num)
