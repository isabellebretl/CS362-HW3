# File: leapyear.py
# Author: Isabelle Bretl
# Date: 04.20.2021
# Input: The user will enter a year
# Output: The program will print a statement regarding whether
# or not the given year is a leap year
# Note: Copied from my hw1 assignment for cs362

print('Enter a year: ')
year = input()
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('{} is a leap year.'.format(year))
        else:
            print('{} is not a leap year.'.format(year))
    else:
        print('{} is a leap year.'.format(year))
else:
    print('{} is not a leap year.'.format(year))