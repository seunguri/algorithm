'''
1. connected component, 이동 수가 칸에 적혀있음.
2. BFS, 
3. 
4. DFS는 시간이 오래 걸린다.
5. Implement the solution
'''
from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx = [0 , 1]
dy = [1, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        visited[x][y] = True
        move = graph[x][y]
        
        if graph[x][y] == -1:
            return True

        for i in range(2):
            nx = x + dx[i] * move
            ny = y + dy[i] * move
            if nx < N and ny < N and not visited[nx][ny]:
                q.append((nx, ny))

if bfs(0, 0):
    print('HaruHaru')
else:
    print('Hing')