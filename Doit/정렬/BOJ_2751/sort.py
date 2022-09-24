import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
bubble = []

for i in range(n):
    bubble.append(int(sys.stdin.readline()))

# print(bubble)

bubble.sort()

for i in bubble:
    print(i)