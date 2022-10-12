import sys

sys.stdin = open("input.txt")
from collections import deque


def bfs(x, y):
    cnt = 1
    queue = deque()
    queue.append([x, y])
    matrix[x][y] = 0
    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                queue.append([nx, ny])
                cnt += 1
    return cnt


"""
    01
10  11  12
    21
"""
# 상 하 좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())  # 세로 / 가로
matrix = [list(map(int, input().split())) for _ in range(n)]
# 그림 개수
pic = 0
# 넓이
area = []

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            # bfs(i, j)
            pic += 1
            area.append(bfs(i, j))

if not area:
    print(0)
    print(0)
else:
    print(pic)
    print(max(area))
