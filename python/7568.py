import sys

input = sys.stdin.readline

n = int(input())
wh_list = []
score_list = [1] * n
for i in range(n):
    x = list(map(int, input().split()))
    wh_list.append(x)

for i in range(n):
    for j in range(n):
        if wh_list[i][0] < wh_list[j][0] and wh_list[i][1] < wh_list[j][1]:
            score_list[i] += 1
for i in score_list:
    print(i)

        
        
