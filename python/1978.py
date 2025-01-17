n = int(input(""))

num = list(map(int, input().split()))
prime = 0
for i in num:
    if i == 0:
        continue
    remain = [0]*i
    # print(remain)
    for j in range(i):
        remain[j] = i % (j+1)
    if remain.count(0) == 2:
        prime+=1

print(prime)