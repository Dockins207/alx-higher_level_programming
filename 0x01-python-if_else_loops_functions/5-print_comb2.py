#!/usr/bin/python3
for k in range(0, 100):
    if k == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
