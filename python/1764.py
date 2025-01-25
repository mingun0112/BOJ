import sys

input = sys.stdin.readline

n ,m = map(int, input().split())
listen_book = set()
look_book = set()

for _ in range(n):
    name = input().strip()
    listen_book.add(name)

for _ in range(m):
    name = input().strip()
    look_book.add(name)

result = listen_book & look_book

result = sorted(result)

print(len(result))
for i in result:
    print(i)
