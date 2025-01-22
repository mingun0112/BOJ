import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

target = list(map(int, input().split()))

m = int(input())

t = list(map(int, input().split()))
counted_t = []
counter = Counter(target)
# print(counter)
for i in t:
    counted_t.append(counter[i])

# print(counted_t)

print(" ".join(map(str, counted_t)))

