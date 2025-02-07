import sys

input = sys.stdin.readline

n = int(input())

x= list(map(int, input().split()))

unq_x=list(set(x))

unq_x.sort()

idx = [i for i in range(len(unq_x))]
# print(idx)
# print(unq_x)
num_idx_dict ={key: value for key, value in zip(unq_x, idx)}


for i in x:
    print(num_idx_dict[i],end=' ')
# print(num_idx_dict)