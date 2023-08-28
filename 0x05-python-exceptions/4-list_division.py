#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            value_1 = my_list_1[i] if i < len(my_list_1) else 0
            value_2 = my_list_2[i] if i < len(my_list_2) else 1  # Avoid division by zero
            division_result = value_1 / value_2
        except ZeroDivisionError:
            print("division by 0")
            division_result = 0
        except (TypeError, ValueError):
            print("wrong type")
            division_result = 0
        except IndexError:
            print("out of range")
            division_result = 0
        finally:
            result_list.append(division_result)

    return result_list
