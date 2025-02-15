import sys
from collections import deque
input = sys.stdin.readline

N ,K = map(int, input().split())

visited = [0]*(100001)
def bfs():
    queue = deque()
    queue.append(N)


    while queue:
        x=queue.popleft()
        if x == K:
            print(visited[x])
            break
        for j in (x-1,x+1,2*x):
            if 0 <= j <= 100000 and visited[j] == 0:
                visited[j]=visited[x]+1
                queue.append(j)
bfs()

