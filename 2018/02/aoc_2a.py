# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 20:54:13 2021

@author: Jonatan
"""

def parse_line(line):
    ret = {}
    cnt = {}
    for c in line:
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1
            
    for dupes in cnt:
        if cnt[dupes] == 2:
            ret[2] = 1
        elif cnt[dupes] == 3:
            ret[3] = 1
            
    return ret
    

def main():
    two = 0
    three = 0
    with open("input.txt") as file:
        for line in file:
            res = parse_line(line.rstrip())
            if 2 in res:
                two += 1
            if 3 in res:
                three += 1
    print(two*three)

if __name__ == "__main__":
    main()