#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        uppercase_lettet = chr(ord(letter) - 32)
        print("{}".format(uppercase_letter), end="")
    print()
