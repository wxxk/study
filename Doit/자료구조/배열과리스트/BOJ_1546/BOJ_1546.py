import sys

sys.stdin = open("input.txt")

n = int(input())
score = list(map(int, input().split()))

# print(score)

# 최대값 찾기
max = 0
# print(score)
for i in range(len(score)):
    if score[i] > max:
        max = score[i]

# print(max)

# 점수 고치기
# (A + B + C) * 100 / M /3
# A+B+C = sum(score)
sum_score = sum(score)
print(sum_score * 100 / max / n)
