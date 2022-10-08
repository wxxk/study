import sys
sys.stdin = open('input.txt')

from collections import deque
def bfs(matrix, a, b):
    queue = deque()
    queue.append((a, b))
    matrix[a][b] = 0        # 방문 처리

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                queue.append((nx, ny))
    return 


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
t = int(input())

for i in range(t):
    N, M, K = map(int, input().split())
    # 가로길이 M / 세로길이 N
    cnt = 0

    matrix = [[0] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1

    # print(matrix)

    for a in range(N):
        for b in range(M):
            if matrix[a][b] == 1:
                bfs(matrix, a, b)
                cnt += 1
    print(cnt)
