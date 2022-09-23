# 계수정렬
# 특정조건이 부합할 때만 사용할 수 있지만 매우 빠른 알고리즘
# 데이터의 크기 범위가 제한되어 정수형태로 표현할 수 있을 때 사용 가능
# 시간 복잡도 최악의 경우에도 O(N+K)

import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
counting = [0] * 10000        # 데이터를 담을 수 있는 list생성

for i in range(n):
    number = int(sys.stdin.readline())
    counting[number-1] += 1

for j in range(len(counting)):
    for k in range(counting[j]):
        print(j+1)