#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
msg = "Last digit of {} is {} and is ".format(number, last_digit)

if last_digit > 5:
    print(msg + "greater than 5")
elif last_digit == 0:
    print(msg + "0")
else:
    print(msg + "less than 6 and not 0")
