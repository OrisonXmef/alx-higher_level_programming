#!/usr/bin/python3
def remove_char_at(s, n):
    if n < 0 or n >= len(s):
        return s

    result = ""
    for i in range(len(s)):
        if i != n:
            result += s[i]

    return result

# Example usage:
original_string = "Hello, World!"
position_to_remove = 7
result = remove_char_at(original_string, position_to_remove)
print(result)

