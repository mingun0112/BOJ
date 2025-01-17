while True:
    tri = sorted(list(map(int, input().split())))
    heru = tri[2]
    ausar = tri[1]
    auset = tri[0]
    if heru == 0 and ausar == 0 and auset == 0:
        break
    if heru**2 == auset**2 + ausar**2:
        print("right")
    else:
        print("wrong")