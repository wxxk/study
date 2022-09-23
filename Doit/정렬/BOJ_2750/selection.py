# 선택정렬
# 최대나 최소 데이를 데이터가 나열된 순으로 찾아가며 선택하는 방법
# 시간 복잡도 O(n**2) : 코딩 테스트에서는 많이 사용하지 않음
# 오름차순으로 구할 땐 최소값을 찾아서 맨 앞으로
# 내림차순으로 구할 땐 최대값을 찾아서 맨 앞으로


import sys
sys.stdin = open('input.txt')

n = int(input())
selection = [int(input()) for _ in range(n)]
temp = 0

for i in range(n):
    min = i     # selection에 i번째 있는 수를 min로 설정
    for j in range(i+1, n):     # 정렬된 부분은 범위에서 제외해주기 위해 i+1
        
        # 최소값 찾기 
        if selection[j] < selection[min]:       
            min = j
    
    # swapping
    if selection[min] < selection[i]:
        temp = selection[i]
        selection[i] = selection[min]
        selection[min] = temp
    
# print(selection)

for k in selection:
    print(k)