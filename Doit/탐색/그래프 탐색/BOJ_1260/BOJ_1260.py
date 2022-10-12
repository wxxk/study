import sys
sys.stdin = open('input.txt')
from collections import deque

def DFS(start):
    order.append(start)
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            DFS(i)

def BFS(start):
    # global visited_BFS
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        cur = queue.popleft()
        order.append(cur)
        for i in graph[cur]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M, V = map(int, input().split())
visited = [False] * (N + 1)
# print(visited_DFS)

graph = [[] for _ in range(N+1)]
# print(graph)

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(N+1):
    graph[i].sort()

# print(graph)

order = [] # 방문된 순서 기록
DFS(V)

print(*order)

order = []
visited = [False] * (N + 1)

BFS(V)
print(*order)