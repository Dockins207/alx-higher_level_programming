#!/usr/bin/python3
lowercase_alphabets = []
for i in range(97, 123):
    if i not in(101, 113):
        lowercase_alphabets.append(chr(i))
print(lowercase_alphabets)
