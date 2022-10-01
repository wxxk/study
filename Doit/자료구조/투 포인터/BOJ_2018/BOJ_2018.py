import sys

sys.stdin = open("input.txt")

# 빠른 포인터가 느린 포인터보다 앞서는 경우
# input 값
n = int(input())

# start_index와 end_index 지정
start_index = 1
end_index = 1
count = 1   # 합쳐서 n이 되는 값을 찾는데 index의 마지막 수는 n이라서 +1
sum = 1     

# 투 포인터 이동원칙에 따라서 이동
while end_index != n:           # end_index의 범위는 n까지
    if sum == n:                # 일치할 때
        end_index += 1          # sum < n 상황이랑 동일하게 진행
        sum += end_index        
        count += 1              # 그치만 n과 같은 값을 찾았으므로 count +1
   
    elif sum > n:           
        sum -= start_index      
        start_index += 1
    
    else:
        end_index += 1
        sum += end_index

print(count)
