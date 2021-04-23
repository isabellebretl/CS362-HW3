# File: leapyear.py
# Author: Isabelle Bretl
# Date: 04.20.2021
# Input: The user will enter a year
# Output: The program will print a statement regarding whether
# or not the given year is a leap year
# Note: Copied from my hw1 assignment for cs362
while True:
    try:
        year = int(input("Please enter a number: "))
        break
    except NameError:
        print("Oops!  That was no valid number.  Try again...")
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