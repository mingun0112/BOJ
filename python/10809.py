a=[-1]*(ord('z')-ord('a')+1)
word = input("")

for i in range(len(word)):
    if a[ord(word[i])-97] == -1:
        a[ord(word[i])-97] = i

a = list(map(str, a))
print(" ".join(a))