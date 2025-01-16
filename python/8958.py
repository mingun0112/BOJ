n = int(input(""))

def ox_recognizer(ox):
    result = 0
    o = 0
    for i in ox:
        # print(i)
        if i == "O":
            o += 1
            result += o
            # print(o)
        else:
            o = 0
    print(result)

            

for i in range(0,n):
    ox = list(input(""))
    ox_recognizer(ox)
