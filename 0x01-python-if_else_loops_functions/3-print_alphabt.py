#!/usr/bin/python3
for letters in range(97, 123):
    if letters in [101, 113]:
        continue
    print("{:c}".format(letters), end="")
