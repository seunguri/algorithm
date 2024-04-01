import sys

N, M = map(int, sys.stdin.readline().split())

arr = [0] * N
for i in range(N):
    arr[i] = int(sys.stdin.readline().rstrip())
arr.sort()

left, right = 0, 1
ans = sys.maxsize

while left < N and right < N:
    tmp = arr[right] - arr[left]
    if tmp == M:
        print(M)
        exit(0)
    if tmp < M:
        right += 1
        continue
    left += 1
    ans = min(ans, tmp)
print(ans)