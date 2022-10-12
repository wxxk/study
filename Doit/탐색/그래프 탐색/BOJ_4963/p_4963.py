from collections import deque
import sys

sys.stdin = open("input.txt")


def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    # 방문처리
    matrix[x][y] = 0

    while queue:
        a, b = queue.popleft()

        # 주변 탐색
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]

            # 범위 검사
            # x 값은 위아래로 움직이니까 h
            # y 값은 옆으로 움직이니까 w
            if 0 <= nx < h and 0 <= ny < w and matrix[nx][ny] == 1:
                # 방문처리
                matrix[nx][ny] = 0
                # bfs
                queue.append([nx, ny])


"""
00 01 02
10 11 12
20 21 22
"""
# 가로, 세로, 대각선
# 본인 값은 제외시켜도 됨!
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# 0 0 이 나오면 종료
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    # 섬의 개수
    count = 0

    # 섬
    matrix = [list(map(int, input().split())) for _ in range(h)]

    # BFS
    # 이중리스트 for문을 돌 때 생각!
    # 옆으로 돌고 다음줄로!!!
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
