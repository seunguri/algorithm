'''
1. 비의 양에 따른 모든 경우에서 안전영역의 최대 개수
2. 안전영역 1개는 연경된 인접 영역 덩어리 -> DFS
3. 1부터 모든 영역이 물에 잠길 때 까지의 안전영역을 조사해서 최대개수 도출
4. Propose a alternative solution
5. Implement the solution
'''


def dfs(x, y, rain):
    visited[x][y] = True
    for i in graph[x][y]:
        if not visited[x][y]:
            dfs(i)


N = int(input())
area = []
for _ in range(N):
    area.append(map(int, input().split()))

visited = [[0] * N for _ in range(N)]
rain = 1
while(True):
    dfs(0, 0, rain)
