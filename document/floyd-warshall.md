- 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산함.
- 다이나믹 프로그래밍
- 시간 복잡도가 O(n^3)
  - 노드의 개수가 N일 때, 알고리즘상으로 N번의 단계를 수행함.
  - 각 단계마다 O(N^2)의 연산을 통해 현재 노드를 거쳐가는 모든 경로를 고려함.
  - 문제에서 노드의 개수가 500개 이하인 경우가 많음

## 구현
```python
INF = int(10e9)

# n은 노드의 개수, m은 간선의 개수
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고 INF 로 초기화
graph = [[INF] * (n + 1) for _ in range (n + 1)]

# 자기 자신의 노드로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 간선 정보를 입력 받아 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(n + 1):
    for a in range(n + 1):
        for b in range(n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
```