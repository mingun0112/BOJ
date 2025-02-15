import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    arr, dpt = map(int, input().split())

    graph[arr].append(dpt)
    graph[dpt].append(arr)


def bfs(start):
    visited = [-1] * (N+1)
    q = deque()
    q.append(start)
    visited[start] = 0
    visited[0] = 0
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node]+1
                q.append(next_node)

    return sum(visited)
min_total = int(1e9)
ans = 0
for i in range(1, N+1):
    total = bfs(i)
    if total < min_total:
        min_total = total
        ans = i
        
print(ans)


