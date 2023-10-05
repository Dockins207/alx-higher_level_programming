#!/usr/bin/python3
<<<<<<< HEAD
for h in range (10):
    for t in range (h + 1, 10):
        print(f"{h}{t}", end=', ')
=======
for first_num in range(0, 10):
    for second_num in range(first_num + 1, 10):
        if first_num == 8 and second_num == 9:
            print("{}{}".format(first_num, second_num))
        else:
            print("{}{}".format(first_num, second_num), end=", ")
>>>>>>> a2ea7c396ee9e54e229b5fd45a15d483ae88a4d9
