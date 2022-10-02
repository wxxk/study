num = [3, 7, 13, 15, 23, 35, 38, 41, 46, 49, 55, 67, 68, 72, 77, 86]
target = 55
start = 0
end = len(num) - 1

while start <= end:
    mid = (start+end)//2

    if num[mid] == target:
        print(num[mid])
        print(mid)
        break

    elif num[mid] > target:
        end = mid -1
    
    else:
        start = mid + 1