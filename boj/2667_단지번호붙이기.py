'''
1. connected component, 각각의 경로마다 특징을 저장
2. DFS
3. count recursive/ global, visted use/unuse
4. BFS
5. Implement the solution
'''
def dfs(x, y):
    global count
    count += 1
    visited[x][y] = True
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 1:
            dfs(nx, ny)

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            count = 0
            dfs(i, j)
            result.append(count)
result.sort()
print(len(result))
print(*result, sep='\n')

'''
1. connected component, 각각의 경로마다 특징을 저장
2. DFS
3. Propose a solution
4. BFS
5. Implement the solution
'''
def dfs(x, y, cnt):
    graph[x][y] = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
            cnt = dfs(nx, ny, cnt+1)
    return cnt

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
result = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(dfs(i, j, 1))

result.sort()
print(len(result))
print(*result, sep='\n')