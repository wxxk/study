from audioop import reverse
import sys
sys.stdin = open('1855.txt')

k = int(input())
word = input()
arr = []

for i in range(0, len(word), k):
    # print(i)
    arr.append(list(word[i:i+k]))

for j in range(len(arr)):
    if j%2 != 0:
        arr[j].reverse()

# print(arr)
answer = list(map(list, zip(*arr)))

for k in answer:
    for l in k:
        print(l, end='')


