#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add, subtract, multiply, divide

    sum_add = add(a, b)
    sub_result = subtract(a, b)
    mult_result = multiply(a, b)
    d_result = divide(a, b)

    print("{} + {} = {}".format(sum_add))
    print("{} -{} = {}".format(sub_result))
    print("{} * {} = {}".format(mult_result))
    print("{} / {} = {}".format(d_result))
