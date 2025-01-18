while True:
    
    n = int(input(""))
    if n == 0:
        break

    n = str(n)
    n = list(map(int, n))

    for i in range(len(n)):
        if n[i] == n[len(n)-1-i]:
            result = "yes"

        else:
            result="no"
            break
    print(result)