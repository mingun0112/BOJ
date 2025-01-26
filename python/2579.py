import sys

input = sys.stdin.readline

x = int(input())
stair = [0] * (x + 1)
for i in range(1, x + 1):
    stair[i] = int(input())


dp = [0] * (x+1)

dp[1] = stair[1]
if x > 1:
    dp[2] = stair[1]+stair[2]
for i in range(3,x+1):
    dp[i] = max(dp[i-2]+stair[i], dp[i-3]+stair[i]+stair[i-1])


print(dp[x])