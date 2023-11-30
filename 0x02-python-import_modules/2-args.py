#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1
    args = argv[1:]

    print("{:d} argument{}{}".format(argc, 's' if argc != 1 else '', ':' if argc != 0 else '.'))

    for i, arg in enumerate(args, 1):
        print("{:d}: {}".format(i, arg))
