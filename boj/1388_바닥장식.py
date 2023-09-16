'''
1. 모든 노드를 탐색
2. Define your approach
3. Propose a solution
4. Propose a alternative solution
5. Implement the solution
'''
n, m = map(int, input().split())
graph = [input() for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = 0

def dfs(x, y):
    visited[x][y] = True
    if graph[x][y] == '-':
        for d in [1, -1]:
            dy = d + y
            if  0 < dy < m and not visited[x][dy] and graph[x][dy] == '-':
                dfs(x, dy)
    elif graph[x][y] == '|':
        for d in [1, -1]:
            dx = d + x
            if 0 < dx < n and not visited[dx][y] and graph[dx][y] == '|':
                dfs(dx, y)

for i in range(n):
    for j in range(m):
        if not visited[i][j]: 
                dfs(i, j)
                result += 1
print(result)