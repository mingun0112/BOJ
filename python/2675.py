test_case = int(input(""))

for i in range(0,test_case):
    n, word = input("").split()
    n = int(n)
    word=list(word)    
    # print(n, word)
    result = ""
    for i in word:
        result+=i*n
    
    print(result)