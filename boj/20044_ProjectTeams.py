"""
문제: https://www.acmicpc.net/problem/20044
풀이: 각 팀원의 역량 합의 최소가 최대가 되도록 팀 구성
-> 정렬해서 가장 양 끝단 끼리 팀 하면 됌.
"""

n = int(input())
w = list(map(int, input().split()))

w.sort()
s_min = w[0] + w[-1]
for i in range(1, n):
    s = w[i] + w[-(1 + i)]
    if s < s_min:
        s_min = s

print(s_min)
