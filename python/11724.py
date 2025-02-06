import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

n ,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    u , v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, visited, start):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            dfs(graph, visited, i)
    return
cnt = 0
for i in range(1, n+1):
    if visited[i] == False:
        cnt+=1
        dfs(graph, visited, i)
print(cnt)