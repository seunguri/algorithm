'''
1. connected component 수
2. Define your approach
3. Propose a solution
4. Propose a alternative solution
5. Implement the solution
'''

# def dfs(x, y, graph):
#     graph[x][y] = 0
#     for dx, dy in d:
#         nx, ny = x+dx, y+dy
#         if 0<=nx<len(graph) and 0<=ny<len(graph[0]) and graph[nx][ny] == 1:
#             dfs(nx, ny, graph)
    

# N = int(input())
# d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# for _ in range(N):
#     M, N, K = map(int, input().split())
#     graph = [[0] * M for _ in range(N)]
#     for _ in range(K):
#         i, j = map(int, input().split())
#         graph[j][i] = 1
    
#     count = 0
#     for i in range(N):
#         for j in range(M):
#             if graph[i][j] == 1:
#                 dfs(i, j, graph)
#                 count += 1
#     print(count)

# M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)
# 재귀함수 깊이가 1000이 넘어가면 RecursionError

    

N = int(input())
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for _ in range(N):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        i, j = map(int, input().split())
        graph[j][i] = 1
    
    count = 0
    stack = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                stack.append((i, j))

                while stack:
                    x, y = stack.pop()
                    graph[x][y] = 0
                    for dx, dy in d:
                        nx, ny = x+dx, y+dy
                        if 0<=nx<len(graph) and 0<=ny<len(graph[0]) and graph[nx][ny] == 1:
                            stack.append((nx, ny))
                count += 1
    print(count)