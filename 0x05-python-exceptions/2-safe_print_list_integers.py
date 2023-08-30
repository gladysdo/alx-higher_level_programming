#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integer_count = 0
    
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end=" ")
                integer_count += 1
    except:
        pass
    
    print()  # Newline after printing
    
    return integer_counti
