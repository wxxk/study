import sys
from tempfile import tempdir
from unittest import result

sys.stdin = open("input.txt")

N, K = map(int, input().split())
tem = list(map(int, input().split()))

# 슬라이딩 윈도우
window = sum(tem[:K])
result = []
result.append(window)

for i in range(K, N):  # K = 2, N = 10
    window = window + tem[i] - tem[i - K]
    # for 문안에 인덱스가 더해지고 빼지는 과정
    # [2]  -  [0]
    # [3]  -  [1]
    # [4]  -  [2]
    # [5]  -  [3]
    # [6]  -  [4]
    # [7]  -  [5]
    # [8]  -  [6]
    # [9]  -  [7]

    result.append(window)

print(max(result))
