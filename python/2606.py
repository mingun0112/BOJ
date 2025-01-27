import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

x = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(x):
    a, b = map(int, input().split())
    print(a, b)
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
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
print(bfs(1))

    