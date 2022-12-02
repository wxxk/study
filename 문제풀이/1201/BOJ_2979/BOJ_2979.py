import sys

sys.stdin = open("input.txt")

parking = [0] * 100
A, B, C = map(int, input().split())
result = 0


for i in range(3):
    arr, lea = map(int, input().split())

    for i in range(arr, lea):
        parking[i] += 1

# print(parking)

for i in range(1, len(parking)):
    if parking[i]:
        if parking[i] == 1:
            result += parking[i] * A
        elif parking[i] == 2:
            result += parking[i] * B
        elif parking[i] == 3:
            result += parking[i] * C


print(result)
