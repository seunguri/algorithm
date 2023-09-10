"""
1 <= N <= 100,000, w/k

1. 내림차순 정렬
2. 로프를 병렬 연결하지 않고 들어올릴 수 있는 중량이 더 크면 연결하지 않는다.
-> Kn * n > K(n+1) * n+1, n은 내림차순에 따른 로프 번호
"""

n = int(input())
ropes = [int(input()) for _ in range(n)]

ropes.sort(reverse=True)
# max_w = 0
# for num, rope  in enumerate(ropes):
#     w = rope * (num + 1)
#     if(max_w > w):
#         break
#     else:
#         max_w = w

kvalues = []
for i in range(n):
    kvalues.append(ropes[i] * (i + 1))
print(max(kvalues))