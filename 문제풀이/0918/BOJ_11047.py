import sys
sys.stdin = open('11047.txt')

n, k = map(int, input().split())
coin = []
cnt = 0

for i in range(n):
    coin.append(int(input()))

coin.reverse()

for i in range(n):
    cnt += k//coin[i]
    k = k%coin[i]

print(cnt)