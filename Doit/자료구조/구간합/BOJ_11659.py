import sys

sys.stdin = open("input.txt")

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

sum_num = [0]  # 합 배열(input의 index범위가 1~5이기때문에 0을 추가해서 인덱스 범위를 맞춰준다!)
temp = 0  # 합을 계산하기 위한 임시 변수

# 합 배열 만들기
for i in num:
    temp += i
    sum_num.append(temp)

# 부분합 구하기
for j in range(M):
    x, y = map(int, sys.stdin.readline().split())

    print(sum_num[y] - sum_num[x - 1])
