#!/usr/bin/python3

def add(a, b):
    return a + b


if __name__ == "__main__":
    add = __import__('10-add').add

    print(add(1, 2))
    print(add(98, 0))
    print(add(100, -2))
