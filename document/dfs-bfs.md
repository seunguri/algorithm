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

# 문제 유형
1. connected component
   - 상하좌우로 연결되어 있다고 표현할 수 있으므로 그래프 형태로 모델링
   - 모두 방문하면 카운트
2. 간선의 비용이 모두 같은 최단 경로 문제