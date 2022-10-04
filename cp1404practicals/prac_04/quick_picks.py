import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """ Quick picks lottery ticket generator - choose random sets of numbers"""
    quick_picks_amount = int(input("How many quick picks?: "))
    while quick_picks_amount < 0:
        print("Value must be above 0. ")
        quick_picks_amount = int(input("How many quick picks?: "))

    for i in range(quick_picks_amount):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()