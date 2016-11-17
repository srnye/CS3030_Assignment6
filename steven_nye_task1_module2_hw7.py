#!/usr/bin/env python3
# encoding: utf-8

import steven_nye_task1_module1_hw7 as modFile1
import sys
import csv

"""
steven_nye_task1_module2_hw7.py
Created by Steven R. Nye on Nov 12, 2016
Email: stevennye@mail.weber.edu
Description: Minivan task 
"""

def mod2(fileName):
    """
    Function that loops through lines in CSV file for minivan configurations
    Args:
        name of CSV file
    Returns:
        Nothing
    """
    rowNum = 1
    with open(fileName, 'rt') as csvfile:
        configreader = csv.reader(csvfile)
        for row in configreader:
            if str(row[0]) == 'H1':
                continue
            modFile1.mod1(rowNum, int(row[1].lstrip()), int(row[2].lstrip()), int(row[3].lstrip()), int(row[4].lstrip()), int(row[5].lstrip()), int(row[6].lstrip()), int(row[7].lstrip()), int(row[8].lstrip()), str(row[9]).lstrip())
            print("")
            rowNum = rowNum + 1

def main(argv):
    """
    Main
    Args:
        CSV file
    Returns:
        Nothing
    """
    mod2(str(sys.argv[1]))
    pass

if __name__ == "__main__":
    main(sys.argv[1])
    exit(0)

