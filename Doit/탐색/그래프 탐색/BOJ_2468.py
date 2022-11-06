import sys

sys.stdin = open("input.txt")

from collections import deque


def bfs(x, y, value):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] > value and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
max_num = 0
result = 0

for i in range(N):
    for j in range(N):
        if matrix[i][j] > max_num:
            max_num = matrix[i][j]

for i in range(max_num):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(N):
            if matrix[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i)
                cnt += 1

    #         matrix[j][k] -= 1
    #         if matrix[j][k] <= 0:
    #             matrix[j][k] = 0
    # # print(matrix)

    # for l in range(N):
    #     for m in range(N):
    #         if matrix[l][m] > 0 and not visited[l][m]:
    #             bfs(l, m)
    #             cnt += 1
    # # print(cnt)

    if result < cnt:
        result = cnt

print(result)
