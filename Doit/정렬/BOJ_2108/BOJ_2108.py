import sys

sys.stdin = open("input.txt")

n = int(input())
numbers = []
avg = 0
middle = 0
range_ = 0


for i in range(n):
    numbers.append(int(input()))

numbers.sort()

# 산술평균
avg = round(sum(numbers) / n)
print(avg)

# 중앙값
# print(numbers)
middle = len(numbers) // 2
print(middle)

# 최빈값

mode = {}

for i in range(len(numbers)):
    mode[numbers[i]] = mode.get(numbers[i], 0) + 1
# print(mode)

mx = max(mode.values())

cc = []
for k, v in mode.items():
    if v == mx:
        cc.append(k)

if len(cc) == 1:
    print(cc[0])
else:
    print(cc[1])

print(numbers[-1] - numbers[0])
