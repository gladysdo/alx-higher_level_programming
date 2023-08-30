#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    index = 0
    
    while count < x:
        try:
            element = my_list[index]
            if isinstance(element, int):
                print("{:d}".format(element), end=" ")
                count += 1
            index += 1
        except Exception:
            break
    
    print()  # Print a new line after all integers have been printed
    return count
