t = int(input(""))



for i in range(t):
    k = int(input())
    n = int(input())
    f0 = [x for x in range(1,n+1)]
    for k_1 in range(k):
        for n_1 in range(1, n):
            f0[n_1] += f0[n_1-1]
    print(f0[-1])
    
