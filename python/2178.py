import sys
from collections import deque
N, M = map(int, input().split())

graph = []
for _ in range(N):
    x= list(map(int,input().strip()))
    graph.append(x)

visited=[[0]*(M) for _ in range(N)]

def bfs():
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 1
    while queue:
        x = queue.popleft()

        if x[0] == N-1 and x[1] == M-1:
            print(visited[x[0]][x[1]])
            break

        for i, j in ((x[0], x[1]+1), (x[0], x[1]-1),(x[0]+1, x[1]),(x[0]-1, x[1])):
            if N > i >= 0 and M > j >= 0:
                # print(i,j)
                if graph[i][j] == 1 and visited[i][j] == 0:
                    visited[i][j] = visited[x[0]][x[1]] + 1
                    queue.append((i,j))


bfs()


