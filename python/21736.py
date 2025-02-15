import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
campus = []
# visited = [[False]*(M) for _ in range(N)]
# visited[1][1]=1
# print(visited)
visited = [[False] * M for _ in range(N)] 
# print(visited)
count = 0
# print(visited)
for _ in range(N):
    x = input().strip()
    campus.append(list(x))

current_locate = deque()
for x in range(N):
    for y in range(M):
        if campus[x][y] == "I":
            current_locate.append((x, y))
            visited[x][y]= True
            break 
# print(current_locate)
move = [(1,0), (-1, 0), (0, 1), (0,-1)]
while current_locate:
    # print(current_locate)
    dx, dy = current_locate.popleft()
    # print(x,y)
    for nx, ny in move:
        x = dx+nx
        y = dy+ny
        # print(x,y)
        # print(campus[x][y])
        if (0<=x<N) and (0<=y<M):
            if (campus[x][y] != "X") and (visited[x][y] == False):
                current_locate.append((x,y))
                visited[x][y] = True
                # print(visited)
                if campus[x][y] == "P":
                    count += 1


if count > 0 :
    print(count)
else:
    print("TT")

