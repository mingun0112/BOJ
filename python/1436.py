import sys

input = sys.stdin.readline

n = int(input())
temp = 0
cnt = 1
while cnt <= n:
    temp += 1
    if "666" in str(temp):
        cnt+=1
print(temp)