# 빙산
# 주변에 0 이 몇개있는지 찾기
# 1년 지날때마다 녹여줌
# n년뒤 두덩이 이상 남으면 출력

import sys

sys.stdin = open("input.txt")

from collections import deque

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 함수
def bfs(a, b):
    visited[a][b] = True
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny <= M:
                if matrix[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

                # 주변 물
                # 상하좌우 돌면서 0이면 물 = 주변에 물만금 빙산을 마이너스
                elif not matrix[nx][ny]:
                    water[x][y] += 1


# input
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
year = 0

while True:
    visited = [[False] * M for _ in range(N)]
    water = [[0] * M for _ in range(N)]
    land = 0

    for i in range(N):
        for j in range(M):
            if matrix[i][j] and not visited[i][j]:
                bfs(i, j)
                land += 1

    for i in range(N):
        for j in range(M):
            matrix[i][j] -= water[i][j]
            if matrix[i][j] < 0:
                matrix[i][j] = 0

    if land >= 2:
        print(year)
        break
    elif not land:
        print(0)
        break
    year += 1
