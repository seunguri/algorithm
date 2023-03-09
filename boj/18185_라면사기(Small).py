"""
문제: https://www.acmicpc.net/problem/18185
풀이:
1. i, i+1, i+2의 범위에서 연달아 하나씩 구매하면 할인이기에 무조건 연달아 구매
2. 1개 공장이면 3원, 2개 공장이면 50% 할인, 3개 공장이면 약 66% 할인 이므로 무조건 공장이 더 연속되도록 구매한다.

2 3 2 1의 경우:
A.
- 1 2 1 1: 7
- 0 1 0 1: 14
- 0 0 0 1: 17
- 0 0 0 0: 20

B.
- 1 2 2 1: 5
- 0 1 1 1: 12
- 0 0 0 0: 19
"""

N = int(input())
A = list(map(int, input().split())) + [0] * 2

price = 0
for i in range(N):
    if A[i + 1] > A[i + 2]:
        count = min(A[i], A[i + 1] - A[i + 2])
        A[i] -= count
        A[i + 1] -= count
        price += count * 5

        count = min(A[i], A[i + 1], A[i + 2])
        A[i] -= count
        A[i + 1] -= count
        A[i + 2] -= count
        price += count * 7
    else:
        count = min(A[i], A[i + 1])
        A[i] -= count
        A[i + 1] -= count
        A[i + 2] -= count
        price += count * 7

        count = min(A[i], A[i + 1])
        A[i] -= count
        A[i + 1] -= count
        price += count * 5
    price += A[i] * 3
    A[i] = 0

print(price)
