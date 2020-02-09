"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

from collections import Counter

# Score categories.
# Change the values as you see fit.
YACHT = (lambda dice: 50 if len(Counter(dice).values()) == 1 else 0)
ONES = (lambda dice: 1*Counter(dice)[1])
TWOS = (lambda dice: 2*Counter(dice)[2])
THREES = (lambda dice: 3*Counter(dice)[3])
FOURS = (lambda dice: 4*Counter(dice)[4])
FIVES = (lambda dice: 5*Counter(dice)[5])
SIXES = (lambda dice: 6*Counter(dice)[6])
FULL_HOUSE = (
    lambda dice: sum(dice) 
    if sorted(Counter(dice).values()) == [2, 3] else 0)
FOUR_OF_A_KIND = (
    lambda dice: 4*Counter(dice).most_common(1)[0][0]
    if Counter(dice).most_common(1)[0][1] >= 4 else 0)
LITTLE_STRAIGHT = (lambda dice: 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0)
BIG_STRAIGHT = (lambda dice: 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0)
CHOICE = (lambda dice: sum(dice))


def score(dice, category):
    try:
        return category(dice)
    except Exception:
        print("Invalid dice input. It must be a list with 5 integers")
