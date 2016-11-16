#!/usr/bin/env python3
"""
riley_curtis_task2_module4_hw7.py
Imports riley_curtis_task2_module3_hw7 and uses it to print zip codes from a txt file
"""
import riley_curtis_task2_module3_hw7 as mod3
from urllib.request import urlopen


def main():
    input_file_lines = urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt").read().decode().split()
    for line in input_file_lines:
        print("Enter zip code: " + line)
        mod3.print_bar_code(line)

if __name__ == '__main__':
    main()
    exit(0)
