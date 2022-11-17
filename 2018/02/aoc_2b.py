# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 20:54:13 2021

@author: Jonatan
"""


def main():
    dupes = {}
    with open("input.txt") as file:
        for line in file:
            better_line = line.rstrip()
            for c in range(len(better_line)):
                index_list = list(better_line)
                index_list[c] = '_'
                index_str = ''.join(index_list)
                if index_str in dupes:
                    print(better_line[:c]+better_line[c+1:])
                else:
                    dupes[index_str] = 1
            

if __name__ == "__main__":
    main()