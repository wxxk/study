import sys
sys.stdin = open('insert.txt')

n = int(input())
num = list(map(int, input().split()))
result = 0
for i in range(n-1):
    for j in range(i, -1, -1):
        if num[j] > num[j+1]:
            temp = num[j]
            num[j] = num[j+1]
            num[j+1] = temp

# print(num)
for i in range(1, len(num)+1):
    result += sum(num[:i])
print(result)