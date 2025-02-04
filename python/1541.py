import sys

n = input().strip()

parts = n.split('-')

result = sum(map(int,parts[0].split("+")))

for i in parts[1:]:
    result -= sum(map(int, i.split("+")))



print(result)