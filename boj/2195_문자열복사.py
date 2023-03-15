"""
https://www.acmicpc.net/problem/2195
1. copy(s, p) 를 최소 사용 횟수
2. greedy
3. P와 S 중 더 짧은 길이의 문자열의 수 n. n 부터 -1 의 구간만큼 복사하여 나타날 수 있는 부분이 존재하는 지 확인.
"""


s = input()
p = input()
cnt = 0
idx = 0

for i in range(len(p)):
    if p[idx: i + 1] in s: continue
    cnt += 1
    idx = i

print(cnt + 1)
