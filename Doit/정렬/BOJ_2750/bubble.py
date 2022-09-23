# 버블정렬
# 인접한 두 데이터를 비교해 정렬하는 방법
# 인접한 데이터 간의 swap연산으로 정렬
# 시간 복잡도 O(n**2)

import sys
sys.stdin = open('input.txt')

n = int(input())
bubble = [int(input()) for _ in range(n)]   # input을 리스트로 받기
temp = 0    # swap을 하기 위한 변수

# print(bubble)

for i in range(n-1):    # 왜 n-1인지???
    for j in range(n-1-i):  # n-1-i : 밑에 if문을 돌고 정렬된 데이터의 범위는 제거해주기 위해 -i
        if bubble[j] > bubble[j+1]:
            # swapping 수행 : 위치를 바꿔준다
            temp = bubble[j]    # 임시로 설정한 변수에 가장 앞에 있는 값을 넣어주고
            bubble[j] = bubble[j+1] # 다음에 있는 값을 앞에 있는 값에 넣어주고
            bubble[j+1] = temp  # 다음에 있는 값에 임시로 설정한 변수에 있는 값을 넣어준다.

# print(bubble)

# output에 맞춰서 출력
for k in range(len(bubble)):
    print(bubble[k])