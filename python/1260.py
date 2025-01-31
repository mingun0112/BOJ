import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

def bfs(start):
    queue = deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    count = 0
    # print(queue)
    while queue:
        v= queue.popleft()
        count += 1
        for i in graph[v]:
            # print(i, visited)
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return count - 1



# def bfs():
graph = [[] for _ in range(n+1)]
print(graph)
for _ in range(n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

    dfs(graph)

print(bfs(v))

