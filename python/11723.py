import sys 

input = sys.stdin.readline

n = int(input())
s= set()
for _ in range(n):
    order = input().split()
    if len(order) == 2:
        order[1] = int(order[1])

    if order[0] == "add":
        s.add(order[1])
    elif order[0] == "remove":
        s.discard(order[1])
    elif order[0] == "check":
        if order[1] in s:
            print(1)
        else:
            print(0)

    elif order[0] =="toggle":
        if order[1] in s:
            s.discard(order[1])
        else:
            s.add(order[1])

    elif order[0] =="all":
        s=set(x for x in range(1,21))

    elif order[0] =="empty":
        s=set()

    # print(s)



    