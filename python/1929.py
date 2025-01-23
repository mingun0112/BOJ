import sys
import math

input = sys.stdin.readline

m, n = map(int,input().split())

prime_list = [0 for _ in range(n+1)]
prime_list[0] = prime_list[1] = 1
# print(prime_list)

for i in range(2, int(math.sqrt(n))+1):
    if prime_list[i] == 0:
        j = 2
        while j*i <= n:
            prime_list[i*j] = 1
            j+=1

# print(prime_list)
for i in range(m, n+1):
    if prime_list[i] == 0:
        print(i)

# print(prime_list)