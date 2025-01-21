# import sys

# input = sys.stdin.readline
# n = ""

setense_list = []
while True:
    # n = input().strip()
    n = input()
    if n == ".":
        break
    setense_list.append(n)
    # print(setense_list)

def checker(s):
    stack = []

    for char in s:
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if not stack:
                return False
            top = stack.pop()
            if char == ")" and top != "(":
                return False
            if char == "]" and top != "[":
                return False

    return not stack


for i in setense_list:
    if checker(i):
        print("yes")
    else:
        print("no")
