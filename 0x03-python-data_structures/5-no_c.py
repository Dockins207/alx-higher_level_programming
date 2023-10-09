#!/usr/bin/python3
def no_c(my_string):
    string2 = [r for r in my_string if r != 'c' and r != 'C']
    return ("".join(string2))
