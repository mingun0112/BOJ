from collections import deque
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
queue = deque(i for i in range(1,n+1))
# print(queue)
result = []
while queue:
    queue.rotate(-(k-1))
    # print(queue)
    result.append(queue.popleft())
        
print("<"+ ", ".join(map(str, result))+">")


