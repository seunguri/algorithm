# 자료구조

## Stack

- 섭입후출
- list의 append(), pop()의 시간복잡도는 상수시간 O(1)임.
- stack[::-1] : 최상단 원소부터 출력, 스택에서 최상단이라는 것은 가장 나중에 들어온 것

## Queue

- 선입선출
- from collections import deque
  - list를 이용하면 시간복잡도가 올라감
  - stack과 queue의 장점을 모두 합함. : append(), popleft()
  - 오른쪽으로 들어와서 왼쪽으로 나가는 것으로 이미징
- queue.reverse(): 나중에 들어온 원소부터 출력

## Recursive Function

- 함수 호출 시 메모리 내부의 스택 프레임에 쌓임 > 스택 대신 재귀함수 이용
- 종료 조건
- 점화식을 사용해서 반복문보다 코드가 간결함
  - factorial: 0! == 1! == 1
  - 유클리드 호제법: A와 B의 최대공약수는 B와 R의 최대공약수 A > B
- 반복문이 더 유리할 수 있음.

# DFS(Depth First Search)

- stack
- 문제에서 나오는 노드 번호와 리스트 인덱스를 일치하는게 헷갈리지 않음

```python
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
```

1. 모든 노드를 방문하고자 하는 경우
2. 깊이 우선 탐색(DFS)이 너비 우선 탐색(BFS)보다 간단
3. 검색 속도 자체는 너비 우선 탐색(BFS)에 비해서 느림

# BFS(Breadth First Search)

- queue

```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque(start)
    visited[start] = True
    while queue:
      v = queue.popleft()
      for i in graph[v]:
        if not visited[i]:
          queue.append(i)
          visited[i] = True
```

두 노드 사이의 최단 경로를 찾고 싶을 때
ex) 지구 상에 존재하는 모든 친구 관계를 그래프로 표현한 후 Sam과 Eddie사이에 존재하는 경로를 찾는 경우

- 깊이 우선 탐색의 경우 - 모든 친구 관계를 다 살펴봐야 할지도 모름
- 너비 우선 탐색의 경우 - Sam과 가까운 관계부터 탐색

# 문제 유형

1. connected component
   - 상하좌우로 연결되어 있다고 표현할 수 있으므로 그래프 형태로 모델링
   - 모두 방문하면 카운트
2. 간선의 비용이 모두 같은 최단 경로 문제

DFS, BFS: 특징에 따라 사용에 더 적합한 문제 유형

- 그래프의 모든 정점을 방문하는 것이 주요한 문제
  단순히 모든 정점을 방문하는 것이 중요한 문제의 경우 DFS, BFS 두 가지 방법 중 어느 것을 사용하셔도 상관없습니다.
  둘 중 편한 것을 사용하시면 됩니다.
- 경로의 특징을 저장해둬야 하는 문제
  예를 들면 각 정점에 숫자가 적혀있고 a부터 b까지 가는 경로를 구하는데 경로에 같은 숫자가 있으면 안 된다는 문제 등, 각각의 경로마다 특징을 저장해둬야 할 때는 DFS를 사용합니다. (BFS는 경로의 특징을 가지지 못합니다)
- 최단거리 구해야 하는 문제
  미로 찾기 등 최단거리를 구해야 할 경우, BFS가 유리합니다.
  왜냐하면 깊이 우선 탐색으로 경로를 검색할 경우 처음으로 발견되는 해답이 최단거리가 아닐 수 있지만,
  너비 우선 탐색으로 현재 노드에서 가까운 곳부터 찾기 때문에경로를 탐색 시 먼저 찾아지는 해답이 곧 최단거리기 때문입니다.

이밖에도

- 검색 대상 그래프가 정말 크다면 DFS를 고려
- 검색대상의 규모가 크지 않고, 검색 시작 지점으로부터 원하는 대상이 별로 멀지 않다면 BFS

---

출처

- https://velog.io/@lucky-korma/DFS-BFS%EC%9D%98-%EC%84%A4%EB%AA%85-%EC%B0%A8%EC%9D%B4%EC%A0%90
- https://www.youtube.com/watch?v=7C9RgOcvkvo
