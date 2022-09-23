import sys
sys.stdin = open('1855.txt')

n = int(input())
s = input()
arr = []

for i in range(0, len(s), n):
    arr.append(s[i:i+n])

for i in range(len(arr)):
    if i % 2 != 0:
        arr[i] = reversed(arr[i])

print(arr[i])