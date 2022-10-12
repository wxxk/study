import sys

sys.stdin = open("input.txt")

def DFS(start):
    order.append(start)
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            DFS(i)



n, m = map(int, input().split())
graph = [[] for _ in range(m+1)]

# 인접리스트로 그래프를 표현
for i in range(1, m+1):
    x, y = map(int, input().split())
    graph[x].append(y)
# print(graph)

# 도는 순서를 기록할 변수
order = []

# 방문리스트
visited = [False] * (n + 1)
print(visited)

# DFS
DFS(1)
print(order)