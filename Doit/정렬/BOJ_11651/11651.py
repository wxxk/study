import sys
sys.stdin = open('input.txt')

n = int(input())
numbers = []

for i in range(n):
    x, y = map(int, input().split())
    numbers.append((x, y))

# print(numbers)

numbers.sort(key = lambda x:(x[1], x[0]))

for i in (numbers):
    print(*i)