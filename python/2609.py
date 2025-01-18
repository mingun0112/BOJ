n = input().split()
n = sorted(list(map(int, n)))
a, b = n[0], n[1]
gcd = 0
# print(a, b)
for i in range(a, 0, -1):
    if a % i == 0 and b % i == 0:
        gcd = i
        break
print(gcd)
print(a*b//gcd)