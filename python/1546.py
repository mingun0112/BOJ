

n = int(input(""))
score = list(map(int, input("").split()))

m = max(score)

new_score = list(map(lambda x:x/m*100, score))

print(sum(new_score)/len(new_score))
