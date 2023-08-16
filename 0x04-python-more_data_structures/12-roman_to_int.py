#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    R_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    sum_total = 0
    prev_value = 0

    for i in roman_string:
        value = R_values[i]
        if value > prev_value:
            sum_total += value - 2 * prev_value
        else:
            sum_total += value
        prev_value = value

    return sum_total
