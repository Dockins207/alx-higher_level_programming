#!/usr/bin/python3
def magic_calculation(a, b):
    dd, sub = __import__('magic_calculation_102').add, __import__('magic_calculation_102').sub

    if a < b:
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
            return (c)
        else:
            return (sub(a, b))
