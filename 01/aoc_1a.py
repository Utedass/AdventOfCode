# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 20:54:13 2021

@author: Jonatan
"""

def main():
    print("Yomanshit!")
    
    freq = 0
    with open("input.txt") as file:
        for line in file:
            freq += int(line.rstrip())
            
        print(freq)

if __name__ == "__main__":
    main()