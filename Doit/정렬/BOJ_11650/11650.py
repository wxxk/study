import sys
sys.stdin = open('input.txt')

n = int(input())

numbers = [list(map(int, input().split())) for _ in range(n)]

# print(numbers)

numbers.sort(key = lambda x:(x[0], x[1]))

for i in range(len(numbers)):
    print(*numbers[i])