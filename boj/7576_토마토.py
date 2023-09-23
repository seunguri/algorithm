'''
1. connected componentm visit all component, adjacent component first
2. loop(from all each 1 to adjacent 0)-> max(each count)
3. DFS, BFS
4. Propose a alternative solution
5. Implement the solution
'''
from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((j, i))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<M and 0<=ny<N and graph[ny][nx] == 0:
            queue.append((nx, ny))
            graph[ny][nx] = graph[y][x] + 1

day = 0
for row in graph:
    for i in row:
        if i == 0:
            print(-1)
            exit()
        if day < i:
            day = i
print(day-1)