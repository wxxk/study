# 계수정렬
# 특정조건이 부합할 때만 사용할 수 있지만 매우 빠른 알고리즘
# 데이터의 크기 범위가 제한되어 정수형태로 표현할 수 있을 때 사용 가능
# 시간 복잡도 최악의 경우에도 O(N+K)

import sys
sys.stdin = open('input.txt')

n = int(input())
numbers = [int(input()) for _ in range(n)]
counting = [0] * (n)        # 데이터를 담을 수 있는 list생성

for i in numbers:       # numbers를 돌면서  데이터 값과 동일한 인덱스의 데이터를 1씩 증가
    counting[i-1] += 1      # 숫자와 인덱스  번호를 맞추기 위해 -1

# print(counting)

# 리스트의 첫번째부터 하나씩 그 값만큼 반복하여 인덱스를 출력
for i in range(len(counting)):
    for j in range(counting[i]):    # 그 값만큼 반복
        print(i+1)