import sys
sys.stdin = open('select.txt')

num = list(input())                     # input 받기

for i in range(len(num)):
    max = i                             # 제일 앞의 값을 max값으로 놓고                                  
    for j in range(i+1, len(num)):      # list를 돌면서 값을 비교해서 max 재설정
        if num[j] > num[max]:           # max 값보다 뒤에 있는 값이 더 크면
            max = j                     # 그 값이 max 값
    if num[max] > num[i]:               # 구한 max 값과 맨 앞을 비교해서 max가 더 크면
        tmp = num[i]                    # 맨앞과 max 값을 swap
        num[i] = num[max]
        num[max] = tmp

print(''.join(num)) 