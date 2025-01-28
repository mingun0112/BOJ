import sys

input = sys.stdin.readline

n , m =map(int, input().split())

num = list(map(int, input().split()))
prefix_sum = [0] * (n+1)
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + num[i-1]

for _ in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b]-prefix_sum[a-1])