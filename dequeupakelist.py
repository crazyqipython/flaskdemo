#!/usr/bin/python
from collections import deque

def search(f,match,number):
    previous_lines=deque(maxlen=number)
    for line in f:
        if match in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__=="__main__":
    with open("encodedecode.txt",'r') as f:
        for line, prelines in search(f,'encode',3):
            for pline in prelines:
                print pline, ''
            print line, ''
            print '_'*20

