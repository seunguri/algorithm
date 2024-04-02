'''
1. Clarify the problem
    P: 자리, 0: 빈 자리, X: 파티션
    5x5
2. Define your approach
    구현, 맨해튼 거리 2 이내에 P 있을 경우 확인
3. Propose a solution
    - 확인해야하는 방향유닛을 담은 리스트: 왼쪽 위부터 진행하므로 오른쪽~아래/위만 확인 -> !!!!!처음에 위를 확인안함!!!!!
    - 범위를 벗어나면 확인 X
    - P가 거리 이내에 있는데 0이 사이에 있으면 0
4. Propose a alternative solution: BFS
    문제 정의: 출발점 P에서 벽X, 길0 미로에서 도착점 P로 갈 수 있는가
    문제 풀이: BFS, 맨해튼 거리 2보다 크면 멈춤
5. Implement the solution
'''

# 오른쪽 위에도 확인해야함
def check0(place):
    check = [(0, 1), (1, 0)]
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                if j < 3 and place[i][j+1] == "O" and place[i][j+2] == "P": return 0
                elif i < 3 and place[i+1][j] == "O" and place[i+2][j] == "P": return 0
                elif i < 4 and j < 4 and place[i+1][j+1] == "P" and (place[i][j+1] == "O" or place[i+1][j] == "O"): return 0
                for x, y in check:
                    if i+x < 5 and j+y < 5 and place[i+x][j+y] == "P": return 0
    return 1

def check(place):
    check = [(0, 1), (1, 0)]
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                if j < 3 and place[i][j+1] == "O" and place[i][j+2] == "P": return 0
                if i < 3 and place[i+1][j] == "O" and place[i+2][j] == "P": return 0
                elif i < 4 and j < 4 and place[i+1][j+1] == "P" and (place[i][j+1] == "O" or place[i+1][j] == "O"): return 0
                elif i > 0 and j < 4 and place[i-1][j+1] == "P" and (place[i][j+1] == "O" or place[i-1][j] == "O"): return 0

                for x, y in check:
                    if i+x < 5 and j+y < 5 and place[i+x][j+y] == "P": return 0
    return 1

from collections import deque

# 불필요한 방문이 있긴한데 5x5니까 뭐
def bfs(p):
    start = []

    for i in range(5):
        for j in range(5):
            if p[i][j] == "P": start.append([i, j])
    
    for s in start:
        queue = deque([s])
        visited = [[0] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]
        visited[s[0]][s[1]] = 1

        while queue:
            y, x = queue.popleft()

            dx = [1, 0, 0] # 우, 상/하만 확인
            dy = [0, -1, 1]

            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:
                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                    
                    if distance[y][x] <= and p[ny][nx] == "P": return 0
        
    return 1


def solution(places):
    answer = []

    for place in places:
        # answer.append(check(place))
        answer.append(bfs(place))

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))