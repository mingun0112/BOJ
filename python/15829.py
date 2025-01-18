n = int(input(""))

word = list(input(""))
word = list(map(ord, word))
result = 0
for i, num in enumerate(word):
    result += (num-96)*(31**i)

print(result%1234567891)
