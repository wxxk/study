import sys
sys.stdin = open('input.txt')

n = int(input())
num = list(map(int, input().split()))
x = int(input())
num.sort()
i = 0
j = n - 1
count = 0

while i < j:
    if num[i] + num[j] == x:
        count += 1
        i += 1
        j -= 1
    elif num[i] + num[j] > x:
        j -= 1
    elif num[i] + num[j] < x:
        i += 1

print(count)