import sys

input = sys.stdin.readline

n = int(input())

sorting_list = []

for i in range(n):
    sorting_list.append(int(input()))

def merge(left, right):
    sorted_list = []
    l, r = 0, 0
    while len(left) > l and len(right) > r:
        if left[l] < right[r]:
            sorted_list.append(left[l])
            l+=1
        else:
            sorted_list.append(right[r])
            r+=1
    sorted_list.extend(left[l:])
    sorted_list.extend(right[r:])

    return sorted_list

def mergeSort(sorting_list):
    if len(sorting_list) <= 1:
        return sorting_list

    mid = len(sorting_list) // 2
    left = mergeSort(sorting_list[:mid])
    right = mergeSort(sorting_list[mid:])

    return merge(left, right)

sorted_list = mergeSort(sorting_list)

for i in sorted_list:
    print(i)