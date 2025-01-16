import sys
input = sys.stdin.readline()
a, b = map(list,input.split())
diff = 0
print(a,b)
for i, q in enumerate(b):
    print(i)
    if a[i] != q[i]:
        diff +=1