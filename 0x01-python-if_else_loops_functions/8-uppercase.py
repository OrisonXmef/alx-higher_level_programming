#!/usr/bin/env python3
def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the lowercase letter to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print(uppercase_char, end='')
        else:
            # Print the character as is
            print(char, end='')

    # Print a new line after processing the string
    print()

# Example usage:
text = "Hello, World!"
uppercase(text)

