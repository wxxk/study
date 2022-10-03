import sys

sys.stdin = open("input.txt")

N, X = map(int, input().split())
num = list(map(int, input().split()))
window = sum(num[:X])
window_list = []

window_list.append(window)

for i in range(X, N):
    window = window + num[i] - num[i - X]
    window_list.append(window)


# 가장 많이 들어온 방문자 수
result = max(window_list)

if result == 0:
    print("SAD")
else:
    print(result)
    print(window_list.count(result))
