#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
if (number < 0):
    print(f"Last digit of {number} is ", end="")
    print(f"-{abs(number) %10} and is less than 6 and not 0")
else:
    if ((abs(number) % 10) == 0):
        print(f"Last digit of {number} is {abs(number) %10} and is 0")
    elif ((abs(number) % 10 ) < 5):
        print(f"Last digit of {number} is ", end="")
        print(f"{abs(number) %10} and is less than 6 and not 0")
    elif ((abs(number) % 10) > 5):
        print(f"Last digit of {number} is ", end="")
        print(f"{abs(number) %10} and is greater than 5")
