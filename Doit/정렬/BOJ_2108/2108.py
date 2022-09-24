from operator import index
import sys
sys.stdin = open('input.txt')

n = int(input())
numbers = []
avg = 0
middle = 0
mode = []
range_ = 0


for i in range(n):
    numbers.append(int(input()))

numbers.sort()

# # 산술평균
# avg = round(sum(numbers)/n)
# print(avg)

# # 중앙값 
# # print(numbers)
# middle = (len(numbers)//2)
# print(middle)

# 최빈값
print(numbers)
a = set(numbers)
print(a)
for i in a:
    mode.append(numbers.count(i))

print(mode)
print(max(mode))

if mode.count(max(mode)) > 1:
    print(mode)
else:
    print(numbers[mode.index(max(mode))])