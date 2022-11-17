# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 20:54:13 2021

@author: Jonatan
"""

def main():
    freq = 0
    dupes = {}
    while True:
        with open("input.txt") as file:
            for line in file:
                freq += int(line.rstrip())
                if freq in dupes:
                    print(freq)
                    return
                dupes[freq] = 1

if __name__ == "__main__":
    main()