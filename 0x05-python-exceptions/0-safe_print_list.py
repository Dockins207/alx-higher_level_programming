#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for x in range(i):
            print(my_list[x], end=" ")
            
    except IndexError:
        pass
    finally:
        print()
        return min(i, len(my_list))
