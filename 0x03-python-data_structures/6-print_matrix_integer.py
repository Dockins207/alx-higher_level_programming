#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for numbers in row:
            print("{:d}".format(numbers), end="")
            if numbers != row[-1]:
                else:
                    print()