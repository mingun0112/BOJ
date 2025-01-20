import sys

input = sys.stdin.readline
def my_round(x):
    if x - int(x) >= 0.5:
        return int(x)+1
    else:
        return int(x)
n = int(input())
scores = []
for _ in range(n):
    scores.append(int(input()))

# 절사할 개수를 계산합니다.
trim_count = my_round(n * 0.15)

# 점수를 정렬합니다.
scores = sorted(scores)

# 절사한 점수 리스트를 만듭니다.
trimmed_scores = scores[trim_count:n - trim_count]

# 절사한 점수 리스트의 평균을 계산합니다.
if len(trimmed_scores) == 0:
    average = 0
else:
    average = sum(trimmed_scores) / len(trimmed_scores)

# 평균을 반올림하여 출력합니다.
print(my_round(average))

