import sys

input = sys.stdin.readline

n = int(input())


for _ in range(n):
    cloth_shelf = dict()
    x = int(input())
    res = 1

    for _ in range(x):
        cloth, _type = input().strip().split()
        if _type in cloth_shelf:
            cloth_shelf[_type].append(cloth)
        else:
            cloth_shelf[_type]=[cloth]
    for i in cloth_shelf:
        res*=len(cloth_shelf[i])+1
    

    

    print(res-1)