from collections import deque
import sys

sys.stdin = open("input.txt")
"""
00 01 02
10 11 12
20 21 22
"""


def bfs(x, y):
    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    matrix[x][y] = 0
    queue = deque()
    queue.append([x, y])
    while queue:
        a, b = queue.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < h and 0 <= ny < w and matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                queue.append([nx, ny])


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    count = 0
    matrix = []
    for _ in range(h):
        matrix.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)
