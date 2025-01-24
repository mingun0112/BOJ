import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
int_list = []
for _ in range(n):
    x = int(input())
    int_list.append(x)
# print(" ")
print(round(sum(int_list)/n))
# print(int_list)
sorted_list = sorted(int_list)
print(sorted_list[len(sorted_list)//2])
counter = Counter(sorted_list)
most_common = counter.most_common()
max_freq = most_common[0][1]
mode = [num for num, freq in most_common if freq==max_freq ]
if len(mode) > 1:
    print(mode[1])
else:
    print(mode[0])
print(max(sorted_list)-min(sorted_list))
