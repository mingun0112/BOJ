import sys

input = sys.stdin.readline

n = int(input())
coord = []
for i in range(n):
    x, y = map(int, input().split())
    coord.append([x,y])

sorted_coord = sorted(coord, key=lambda x: (x[1], x[0]))
# print(sorted_coord)

for x, y in sorted_coord:
    print(f'{x} {y}')