#!/usr/bin/python3

print(''.join(chr(i) for i in range(ord('z'), ord('a') - 1, -1) if i % 2 == 0), end='')
