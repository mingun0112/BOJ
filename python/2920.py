scale_map = input("").split()
scale_map = list(map(int,scale_map))
result = ""

if scale_map == sorted(scale_map):
    print("ascending")
elif scale_map == sorted(scale_map,reverse=True):
    print("descending")
else:
    print("mixed")
