import sys

input = sys.stdin.readline

k, n = map(int, input().split())

lan_list = []
for _ in range(k):
    l = int(input())
    lan_list.append(l)

start = 1
end = max(lan_list)

while start <= end:
    mid = (start+end) // 2
    count = sum(l//mid for l in lan_list)

    if count >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
