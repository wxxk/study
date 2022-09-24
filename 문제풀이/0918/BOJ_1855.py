from audioop import reverse
import sys
sys.stdin = open('1855.txt')

<<<<<<< HEAD
n = int(input())
s = input()
arr = []

for i in range(0, len(s), n):
    arr.append(s[i:i+n])

for i in range(len(arr)):
    if i % 2 != 0:
        arr[i] = reversed(arr[i])

print(arr[i])
=======
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


>>>>>>> bf8eabcb71b263782402a749f6014b252b4841ac
