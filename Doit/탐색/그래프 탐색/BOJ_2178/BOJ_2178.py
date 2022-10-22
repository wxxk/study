# 미로로 가는 최소 칸수
import sys
sys.stdin = open('input.txt')

from collections import deque

# 4. bfs 함수 / 칸수 체크 
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = matrix[a][b] + 1



# 1. 사방 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 2. input
N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range (N)]
# print(matrix)


# 3. 시작지점 bfs
bfs(0,0)


# 5. 최소 칸수 출력
print(matrix[N-1][M-1])
