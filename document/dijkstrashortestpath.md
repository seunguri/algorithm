# Dijkstra Shortest Path
- 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산함
- 음의 간선이 없음
- 그리디 알고리즘: 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택
- 한 번 처리된 노드의 최단 거리는 고정

## 동작 과정
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중에서 최단 거리가 **가장 짧은 노드 선택** : 그리디
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
5. 3, 4번 반복
## 구현
```python
import sys
input = sys.stdin.readline
INF = int(1e9)

# n은 노드의 개수, m은 간선의 개수
n, m = map(int, input().split())
# 출발 노드 설정
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
# shortest path table
distance = [INF] * (n + 1) 

for _ in range(m):
    from_node, to_node, cost = map(int, input().split())
    graph[from_node].append((to_node, cost))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF: print("INFINITY")
    else: print(distance[i])
```

### Complexity
시간 복잡도는 O(N^2)
- O(N)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색함.
- python 기준으로 1초에 약 2000만번 처리하므로, 최단 경로 문제에서 전체 노드 개수가 5000개 이하면 해결할 수 있음.
  -> 노드가 5000개를 넘으면 우선순위 큐를 사용하자.
  -  방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 Heap 자료구조 이용 

## Priority Queue
- Heap: 트리 구조를 사용하여 삽입, 삭제 시간이 O(logN)
  리스트는 삽입 O(1), 삭제 O(N)

- 최소 힙으로 구현된 파이썬 heapq 라이브러리
```python
import heapq

# O(NlogN): 삽입, 삭제 N번씩
def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
```
## 구현: 우선순위 큐
```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# n은 노드의 개수, m은 간선의 개수
n, m = map(int, input().split())
# 출발 노드 설정
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
# shortest path table
distance = [INF] * (n + 1) 

for _ in range(m):
    from_node, to_node, cost = map(int, input().split())
    graph[from_node].append((to_node, cost))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
```

### Complexity
시간 복잡도는 O(ElogN)
- while문은 노드의 개수 N 이하 횟수만큼 처리함
  - 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총횟수는 최대 간선의 개수(E) 만큼 수행함
- E개의 원소를 우선수위 큐에 삽입하고 모두 삭제하는 연산과 매우 유사함.
  - 시간 복잡도는 O(ElogE)
  - 중복 간선을 포함하지 않는 경우에 O(ElogV)
    - O(ElogE) -> O(ElogN^2) -> O(2ElogN) -> O(ElogN)