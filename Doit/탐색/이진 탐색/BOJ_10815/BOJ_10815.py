import sys

sys.stdin = open("input.txt")

n = int(input())
num = list(map(int, input().split()))
num.sort()
m = int(input())
target_list = list(map(int, input().split()))
result = [0] * m

for i in range(len(target_list)):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if num[mid] == target_list[i]:
            result[i] += 1
            break
        # -10 2 3 6 10
        elif num[mid] > target_list[i]:
            end = mid - 1

        else:
            start = mid + 1

print(*result)
