import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y>=m:
        return
    if ground[x][y] == 1:
        ground[x][y] = -1
        dfs(x-1,y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)


for _ in range(n):
    m, n, k =map(int, input().split())
    ground = [[0]*m for _ in range(n)]
    bug = 0
    # print(ground)
    for _ in range(k):
        y, x = map(int, input().split())
        ground[x][y] = 1
    
    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1:
                dfs(i, j)
                bug += 1
                

    print(bug)

