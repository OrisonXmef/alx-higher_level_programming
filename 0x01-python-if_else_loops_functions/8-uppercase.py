#!/usr/bin/python3

def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print(uppercase_char, end='')
        else:
            print(char, end='')
    print()

def main():
    uppercase("best")
    uppercase("Best School 98 Battery street")

if __name__ == "__main__":
    main()
