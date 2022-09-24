import sys
sys.stdin = open('bubble.txt')

N = int(input())
numbers = []

for _ in range(N):
    numbers.append(int(input()))

for i in range(0, N-1):
    for j in range(0, N-1-i):
        if numbers[j] > numbers[j+1]:
            tmp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = tmp

for k in range(len(numbers)):
    print(numbers[k])