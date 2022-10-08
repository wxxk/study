import sys

sys.stdin = open("input.txt")

# DFS
def DFS(v):
    visited[v] == True
    for i in graph[v]:
        if not visited[i]:
            DFS(i)


n, m = map(int, input().split())
graph = [[] for _ in range(m)]

# 인접리스트로 그래프를 표현
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
# print(graph)


# 방문리스트
visited = [False] * (n + 1)
print(visited)


# DFS
for i in range(1, n + 1):
    if not visited[i]:
        DFS(i)
