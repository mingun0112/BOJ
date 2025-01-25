import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pocketmon_dict = dict()
for i in range(1, n+1):
    pocketmon = input().strip()
    pocketmon_dict[i] = pocketmon
reverse_pocketmon_dict = {v: k for k, v in pocketmon_dict.items()}
for _ in range(m):
    i = input().strip()
    if i.isdigit():
        print(pocketmon_dict[int(i)])
    else:
        print(reverse_pocketmon_dict[i])



    