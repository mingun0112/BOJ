import sys

input = sys.stdin.readline

n = int(input())

lim = n//3
res = 0
sample = []

for i in range(lim+1):
    for j in range(lim+1):
        res = 3*j + 5*i
        if res == n:
            sample.append(i+j)


if len(sample) == 0:
    print(-1)
else:
    print(min(sample))

# print(sample)