import sys

input = sys.stdin.readline
n = int(input())
res = 1
for i in range(n,0,-1):
    res *= i
if "0" not in str(res):
    print(0)
else:
    for i in range(len(str(res)), 1, -1):
        if str(res)[i-1] != "0":
            print(len(str(res))-i)
            break
# print(res)