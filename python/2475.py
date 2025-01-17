code = input("").split(" ")
# print(code)
code = list(map(int, code))
code = list(map(lambda x: x**2, code))
result = sum(code)%10
print(result)