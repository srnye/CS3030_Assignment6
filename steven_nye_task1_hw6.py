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
    """
    This function prints whether a specified sequence of controls is valid or not for a minivan's locking configurations
    Args:
        hr = Header Record
        ld = Left Dashboard switch (0 or 1)
        rd = Right Dashboard switch (0 or 1)
        cl = Child Lock switch (0 or 1)
        ml = Master unLock switch (0 or 1)
        li = Left Inside handle (0 or 1)
        lo = Left Oustide handle (0 or 1)
        ri = Right Inside handle (0 or 1)
        ro = Right Outside handle (0 or 1)
        gs = Gear Shift position (P, N, D, 1, 2, 3 or R)
    Returns:
        Nothing
    """
    print("Heading Record " + str(hr) + ":")
    print("Left dashboard switch (0 or 1): " + str(ld))
    print("Right dashboard switch (0 or 1): " + str(rd))
    print("Child lock switch (0 or 1): " + str(cl))
    print("Master unlock switch (0 or 1): " + str(ml))
    print("Left inside handle (0 or 1): " + str(li))
    print("Left outside handle (0 or 1): " + str(lo))
    print("Right inside handle (0 or 1): " + str(ri))
    print("Right outside handle (0 or 1): " + str(ro))
    print("Gear shift position (P, N, D, 1, 2, 3 or R): " + gs)

    lOpen = False
    rOpen = False

    if gs != 'P' and gs != 'N' and gs != 'D' and gs != 'R' and gs != 1 and gs != 2 and gs != 3:
        print("Invalid Record: Both doors stay closed.")
        return

    if gs != 'P':
        print("Both doors stay closed.")
        return

    if ml != 1:
        print("Both doors stay closed.")
        return

    #Check for dashboard switches
    if rd == 1 and ld == 1:
        print("Both doors open.")
        return
        
    elif rd == 1:
        rOpen = True
        
    elif ld == 1:
        lOpen = True

    #Check outside handles
    if lo == 1:
        lOpen = True

    if ro == 1:
        rOpen = True

    #Check inside handles
    if li == 1 and cl == 0:
        lOpen = True

    if ri == 1 and cl == 0:
        rOpen = True

    #Print results
    if lOpen == True and rOpen == True:
        print("Both doors open.")
        return
    elif lOpen == True and rOpen == False:
        print("Left door is open.")
        return
    elif lOpen == False and rOpen == True:
        print("Right door is open.")
        return
    else:
        print("Both doors stay closed.")
        return



def main():
    mod1(1, 0, 1, 0, 1, 0, 1, 0, 0, 'P')
    mod1(2, 1, 0, 0, 1, 0, 1, 0, 0, 'D')
    mod1(3, 1, 0, 0, 1, 0, 1, 0, 0, 'E') 
    pass

if __name__ == "__main__":
    main()
    exit(0)

