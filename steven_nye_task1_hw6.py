#!/usr/bin/env python3
# encoding: utf-8

import sys

"""
steven_nye_task1_hw6.py
Created by Steven R. Nye on Nov 12, 2016
Email: stevennye@mail.weber.edu
Description: Minivan task 
"""

def mod1(hr, ld, rd, cl, ml, li, lo, ri, ro, gs):
    print("Heading Record " + hr + ":")
    print("Left dashboard switch (0 or 1): " + ld)
    print("Right dashboard switch (0 or 1): " + rd)
    print("Child lock switch (0 or 1): " + cl)
    print("Master unlock switch (0 or 1): " + ml)
    print("Left inside handle (0 or 1): " + li)
    print("Left outside handle (0 or 1): " + lo)
    print("Right inside handle (0 or 1): " + ri)
    print("Right outside handle (0 or 1): " + ro)
    print("Gear shift position (P, N, D, 1, 2, 3 or R): " + gs)

    if gs != 'P' or gs != 'N' or gs != 'D' or gs != 'R' or gs != 1 or gs != 2 or gs != 3:
        print("Invalid Record: Both doors stay closed.")


def main():
    
    pass

if __name__ == "__main__":
    main()
    exit(0)

