import sys

sys.stdin = open("input.txt")
from collections import deque

# 김유영 도움


def bfs(x, y):
    cnt = 1
    queue = deque()
    queue.append([x, y])
    maps[x][y] = 1

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < M and 0 <= ny < N and maps[nx][ny] == 0:
                cnt += 1
                maps[nx][ny] = 1
                queue.append((nx, ny))
    return cnt


M, N, K = map(int, input().split())

maps = [[0] * N for _ in range(M)]

for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(M - ry, M - ly):
        for j in range(lx, rx):
            maps[i][j] = 1
# print(maps)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
area = []

# 5 7 3
for i in range(M):
    for j in range(N):
        if maps[i][j] == 0:
            area.append(bfs(i, j))


area.sort()
print(len(area))
print(*area)
