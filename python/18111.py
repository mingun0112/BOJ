import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())

field = []

for _ in range(n):
    x = list(map(int, input().split()))
    field.append(x)

ans = int(1e9)
glevel = 0

for p in range(257):
    use_block = 0
    put_block = 0

    for i in range(n):
        for j in range(m):
            if field[i][j] > p:
                put_block += field[i][j]-p
            else:
                use_block += p-field[i][j]
    if use_block > b+put_block:
        continue
    

    count = use_block+put_block*2

    if count <= ans:
        ans = count
        glevel = p


print(ans, glevel)
    




