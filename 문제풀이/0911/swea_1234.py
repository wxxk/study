import sys
sys.stdin = open('1234.txt')

T = 10

for tc in range(1, T+1):
    N, num = input().split()
    N = int(N)
    stack = []

    for i in num:
        if stack:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    result = "".join(stack)
    print(f"#{tc} {result}")