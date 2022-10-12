import sys
from collections import deque
sys.stdin = open('input.txt')

# 1. N위치에서 K위치로 가는 최단시간 찾기
# 2. 최단 거리는 BFS를 이용
# 3. 이동하는 위치 X-1 / X+1 / X*2
# 4. 최소 최대값을 넘지 않도록 조건문 사용
# 5. 방문 위치를 표시하기
# 6. 각 방문에 대한 표시를 노드 깊이로 설정하면, 해당 위치까지 걸린 시간을 대표 하는 값

def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        cur = queue.popleft()
        if cur == k:
            print(matrix[cur])
            break
        
        for next in (cur-1, cur+1, cur*2):
            if 0 <= next <= max and not matrix[next]:
                matrix[next] = matrix[cur] + 1      # 깊이를 들어갈 때마다 1씩 더해서 거리만큼 걸린시간을 표시
                queue.append(next)
    return


n, k = map(int, input().split())
max = 100001
matrix = [0]*max

bfs()
