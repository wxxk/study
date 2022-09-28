import sys

sys.stdin = open("input.txt")
n = int(input())
numbers = list(map(int, input()))
sum = 0

for i in range(len(numbers)):
    sum += numbers[i]

print(sum)
