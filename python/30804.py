import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

x= list(map(int, input().split()))

start, end = 0, 1

kind =[x[0]]

while True:
    if len(kind) == 1:
        if x[end] not in kind:
            kind.append(x[end])
    else:
        if x[end] not in kind:
            start += 1
    
    if 
    end += 1



