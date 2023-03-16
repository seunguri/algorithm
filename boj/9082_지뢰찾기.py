"""
https://www.acmicpc.net/problem/9082

2*N 판에서 지뢰가 맨 앞, 맨 뒤에 있으면 2칸에 영향을 미치고, 나머지에 있으면 3칸에 영향을 줌.
지뢰의 위치에 대해 불가능한 값은 주어지지 않으므로, 블록 주위에 지뢰가 몇 개 있는지(입력 첫 번째줄)를 모두 더한 값 sum으로 결과를 구할 수 있음.

1. sum%3==0: 맨 앞과 맨 뒤에 지뢰가 없다. 3으로 나눈 값이 정답
2. sum%3==1: 앞과 뒤 모두에 지뢰를 배치하고, (sum-4)/3개의 지뢰를 배치
3. sum%3==2: 앞 또는 뒤에 지뢰를 배치하고, (sum-2)/3개의 지뢰를 배치.
"""

t = int(input())

for _ in range(t):
    n = input()
    sum_near_mine = sum(map(int, list(input())))
    mark_mine = input()
    print((sum_near_mine + 2) // 3)
    