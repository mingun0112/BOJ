n = int(input(""))
size = list(map(int, input("").split()))
t, p = map(int, input("").split())

total_t = 0
for i in size:
    if i == 0:
        continue
    if i % t == 0:
        total_t+=i//t
    else:
        total_t+=i//t+1
print(total_t)
        
print(n//p, n%p)