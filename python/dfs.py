import sys
from collections import deque

input = sys.stdin.readline
n, m, v=map(int, input().split())

graph = [[] for _ in range(n+1)]


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] != True:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v= queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            # print(visited)
            if visited[i] != True:
                queue.append(i)
                visited[i] = True


for _ in range(m):
    arrival, departure = map(int, input().split())

    graph[arrival].append(departure)
    graph[departure].append(arrival)

for i in range(1, n+1):
    graph[i] = sorted(graph[i])
dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)
dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)





