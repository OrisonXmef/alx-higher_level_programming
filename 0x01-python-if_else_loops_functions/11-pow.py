#!/usr/bin/python3

def pow(a, b):
    return a ** b


if __name__ == "__main__":
    pow = __import__('11-pow').pow

    print(pow(2, 3))
    print(pow(98, 2))
    print(pow(5, 0))
