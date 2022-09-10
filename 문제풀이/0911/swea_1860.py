import sys
sys.stdin = open('1860.txt')

T = int(input())

for i in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    result = "Possible"
    for j in range(N):
        bread = (arr[j] // M) * K - (j+1)

        if bread < 0:
            result = "Impossible"
            break

    print("#{} {}".format(i, result))