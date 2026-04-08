#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i in range(len(roman_string)):
        if i < len(roman_string) - 1 and roman[roman_string[i]] < roman[roman_string[i + 1]]:
            total -= roman[roman_string[i]]
        else:
            total += roman[roman_string[i]]
    return total
