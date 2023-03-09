"""
문제: https://www.acmicpc.net/problem/1260
풀이: 시간 제한이 2초이고, 0 <=정점 N <=1000, 0 <= 간선 M <=10000
./document/dfs-bfs.md
인접 행렬로 구현한 경우: O(N^2), 인접 리스트로 구현한 경우: O(N + M)
"""
from collections import deque


def dfs(V):
    dfs_visited[V] = True
    print(V, end=" ")

    for i in graph[V]:
        if not dfs_visited[i]:
            dfs(i)


def bfs(V):
    queue = deque([V])
    bfs_visited[V] = True

    while queue:
        s = queue.popleft()
        print(s, end=" ")
        for e in graph[s]:
            if not bfs_visited[e]:
                queue.append(e)
                bfs_visited[e] = True


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N + 1):
    graph[i].sort()

dfs_visited = [False] * (N + 1)
dfs(V)
print()

bfs_visited = [False] * (N + 1)
bfs(V)
