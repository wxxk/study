import sys
sys.stdin = open('input.txt')

n = int(input())
m = int(input())
num = list(map(int, input().split()))
num.sort()
i = 0 # start 인덱스 
j = n-1 # end 인덱스
count = 0

while i < j:
    if num[i] + num[j] == m:
        count += 1
        i += 1
        j -= 1
    elif num[i] + num[j] < m :
        i += 1
    elif num[i] + num[j] > m :
        j -= 1

print(count)    