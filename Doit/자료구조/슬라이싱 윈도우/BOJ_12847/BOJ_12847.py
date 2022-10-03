import sys

sys.stdin = open("input.txt")

n, m = map(int, input().split())
num = list(map(int, input().split()))
window = 0
answer = []
for i in range(m):
    window += num[i]
# window = sum(num[:m])

answer.append(window)

for i in range(m, n):
    window = window + num[i] - num[i - m]
    answer.append(window)

print(max(answer))
