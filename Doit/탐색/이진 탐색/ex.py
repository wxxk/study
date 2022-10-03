num = [3, 7, 13, 15, 23, 35, 38, 41, 46, 49, 55, 67, 68, 72, 77, 86]
target = 55
start = 0
end = len(num) - 1

while start <= end:
    # 중앙값
    mid = (start + end) // 2

    # target값을 찾았을 경우
    if num[mid] == target:
        print(num[mid])
        print(mid)
        break

    # 중앙값 > 타깃 데이터 : 왼쪽 데이터 셋 선택
    elif num[mid] > target:
        end = mid - 1

    # 중앙값 < 타깃 데이터 : 오른쪽 데이터 셋 선택
    else:
        start = mid + 1
