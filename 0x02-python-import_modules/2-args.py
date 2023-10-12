#!/usr/bin/python3
import sys
argv = sys.argv[1:]
num_args = len(argv)

if num_args == 0:
    print("Number of argument(s): 0.")
    print(".")
else:
    print("Number of argument(s): {}.".format(num_args))
    for i, arg in enumerate(argv):
        print("Argument {}: {}".format(i+1, arg))
