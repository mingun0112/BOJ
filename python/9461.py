import sys

input = sys.stdin.readline

n = int(input())
tri = [ 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]+[0 for _ in range(10, 100)]
# print(tri)
i = 10
while i < 100:
    # print(i)
    tri[i] = tri[i-5]+tri[i-1]
    i+=1

for i in range(n):
    x = int(input())
    # print(tri)
    print(tri[x-1])