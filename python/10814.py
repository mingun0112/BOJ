import sys

input=sys.stdin.readline

n = int(input())

member_list = [[] for _ in range(n)]
for i in range(n):
    t = input().split()
    t[0] = int(t[0])

    member_list[i] = t

# print(member_list)
sorted_list = sorted(member_list, key = lambda x: x[0])
for i in sorted_list:
    i[0] = str(i[0])
    print(" ".join(i))