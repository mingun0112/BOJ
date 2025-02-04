import sys

n = int(input())


paper = []

count_one = 0
count_zero = 0


for _ in range(n):
    row = list(map(int, input().split()))
    paper.append(row)

def div_conq(x, y, N):
    temp = 0
    global count_one
    global count_zero
    for i in range(x, x+N):
        for j in range(y, y+N):
            if paper[i][j] != 0:
                temp+=1
    if temp == 0:
        count_zero+=1
    elif temp == N**2:
        count_one += 1
    else:
        div_conq(x,y, N//2)
        div_conq(x+N//2,y,N//2)
        div_conq(x,y+N//2, N//2)
        div_conq(x+N//2,y+N//2,N//2)
    return
div_conq(0,0,n)
print(count_zero)
print(count_one)

