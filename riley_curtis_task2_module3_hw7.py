#!/usr/bin/env python3
"""
riley_curtis_task2_module3_hw7.py
task 2 module 3 for hw7
Asks user for a zip code then prints the bar code for that zip
"""


def print_digit(d):
    """
    prints the bar code value for the given digit
    :param d:
    :return None:
    """
    if d == 1:
        print(":::||", end="")
    elif d == 2:
        print("::|:|", end="")
    elif d == 3:
        print("::||::", end="")
    elif d == 4:
        print(":|::|", end="")
    elif d == 5:
        print(":|:|:", end="")
    elif d == 6:
        print(":||::", end="")
    elif d == 7:
        print("|:::|", end="")
    elif d == 8:
        print("|::|:", end="")
    elif d == 9:
        print("|:|::", end="")
    elif d == 0:
        print("||:::", end="")
    else:
        print("Invalid digit")


def print_bar_code(zip_code):
    """
    prints the bar code for the given zip
    :param zip_code:
    :return None:
    """
    zip_sum = 0
    check_digit = 0

    print("|", end="")

    for i in zip_code:
        i = int(i)
        print_digit(i)
        zip_sum += i

    while zip_sum % 10 != 0:
        check_digit += 1
        zip_sum += 1

    print_digit(check_digit)
    print("|")


def main():
    user_input = input("Enter a zip code: ")
    print_bar_code(user_input)


if __name__ == '__main__':
    main()
    exit(0)
