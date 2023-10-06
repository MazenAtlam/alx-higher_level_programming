#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args_len = len(argv)
    sum = 0
    for i in range(1, args_len):
        sum += int(argv[i])
    return sum
