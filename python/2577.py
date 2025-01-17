a = int(input(""))
b = int(input(""))
c = int(input(""))

ans = str(a*b*c)
print(ans.count("0"))
for i in range(1, 10):
    print(ans.count(str(i)))