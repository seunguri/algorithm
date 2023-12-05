'''
1. problem definition
    방향 없는 간선 ->
    connected component ->

2. Define your approach
    알고리즘: DFS
    자료구조: 
    - edges => 인덱스+1이 정점 번호이며 리스트로 연결된 정점을 담고있는 이차원배열
    - visited => 같은 간선을 한 번만 주어지므로 일차원 배열
3. 
    1. 연결 요소 시작: 정점을 방문하지 않았으면 df메서드를 호출한다. 
    2. 연결 요수 탐색: dfs 재귀함수를 사용하여 현재 정점과 연결된 정점을 방문처리한다. 
    3. 개수 + 1: 모든 연결된 정점을 방문했으면 재귀함수를 종료하고 1번으로 돌아간다.

4. BFS
5. Implement the solution

* 시간초과: sys.stdin.readline 으로 입력받자
    - input()
        1. 인자의 문자를 출력하고 사용자 입력 대기 
        2. 사용자 키 입력 시 데이터가 하나씩 버퍼에 입력
        3. 개행 문자 입력 종료 간주
        4. 모든 입력을 문자열로 변환하고 줄바꿈 제거 후 반환
    - sys.stdin.readline()
        1. 화면에 출력 X
        2. 한 번에 읽는 글자수 크기 지정 가능
        3, 2만큼의 입력을 한 번에 읽어와 버퍼에 저장. 
            -> 누를 때마다 데이터 버퍼에 저장하는 input()보다 빠름
                -> 입력이 많아질수록 성능 차이

* 런타임에러: sys.setrecursionlimit(10000) 탐색 길이를 늘려주자
    python, default recursion limit == 1000


'''
import sys
sys.setrecursionlimit(10000) 
input = sys.stdin.readline

def dfs(edges, i, visited):
    visited[i] = True
    for n in edges[i]:
        if not visited[n]: dfs(edges, n, visited)

N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)

answer = 0
visited = [False] * N
for i in range(N):
    if not visited[i]: 
        dfs(edges, i, visited)
        answer += 1

print(answer)