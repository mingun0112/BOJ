import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
int_list = []
for _ in range(n):
    x = int(input())
    int_list.append(x)

print(sum(int_list)/n)
print(int_list)
sorted_list = sorted(int_list)
print(sorted_list[len(sorted_list)//2])
counter = Counter(sorted_list)

print(1,":",counter)
