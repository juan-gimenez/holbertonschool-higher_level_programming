#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit < 6 and last_digit != 0:
    print('Last digit of {:d} is {:d} and'.format(number, last_digit), end='')
    print(' is less than 6 and not 0')
elif last_digit > 5:
    print('Last digit of {:d} is {:d} and'.format(number, last_digit), end='')
    print(' is greater than 5')
elif last_digit == 0:
    print('Last digit of {:d} is {:d} and'.format(number, last_digit), end='')
    print(' is 0')
