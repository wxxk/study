import sys

sys.stdin = open("input.txt")

n = int(input())

# start_index와 end_index 지정
start_index = 1
end_index = 1
count = 1
sum = 1

while end_index != n:
    if sum == n:
        end_index += 1
        sum += end_index
        count += 1
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index

print(count)
