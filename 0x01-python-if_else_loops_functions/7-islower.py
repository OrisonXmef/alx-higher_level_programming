def islower(c):
    # Check if the ASCII value of the character is between 'a' and 'z'
    return ord('a') <= ord(c) <= ord('z')

# Example usage:
char = 'a'
result = islower(char)
print(f"Is '{char}' lowercase? {result}")

