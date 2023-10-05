#!/usr/bin/python3
for i in range(99):
    fdigit = int(i / 10)
    sdigit = int(i % 10)
    print("{:d}{:d}".format(fdigit, sdigit), end=", ")
print(99)
