import sys

input = sys.stdin.readline

for i in range(3):
    x=input().strip()
    if x not in ["Fizz", "Buzz", "FizzBuzz"]:
        n = int(x)+3-i

if n % 15 == 0:
    print("FizzBuzz")
elif n % 5 == 0:
    print("Buzz")
elif n % 3 == 0:
    print("Fizz")
else:
    print(n)