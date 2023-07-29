import sys
n, m = map(int, input().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
b = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = [ [z + k for z, k in zip(x, y)] for x, y in zip(a, b)]
for i in result:
    print(*i)
