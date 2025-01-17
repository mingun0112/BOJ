n = int(input(""))

def find_room(h, w, n):
    floor = n%h
    room = n // h + 1
    if floor == 0:
        floor = h
        room -=1
    return floor*100 + room
    


for i in range(0,n):
    h, w, n = map(int, input("").split())
    result = find_room(h , w, n)
    print(result)