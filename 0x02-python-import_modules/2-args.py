#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args_len = len(argv) - 1
    print("{}".format(args_len), end=' ')
    if args_len == 0:
        print("arguments.")
    elif args_len == 1:
        print("argument:")
    else:
        print("arguments:")
    for i in range(1, args_len + 1):
        print("{}: {}".format(i, argv[i]))
