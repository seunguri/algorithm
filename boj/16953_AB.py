'''
1. A*2, A1 -> B가 되는 연산의 최솟값
2. greedy top down
3. B가 짝수면 2로 나누고 1이 끝에나오면 제거
4. bfs
5. Implement the solution
'''


from collections import deque
A, B = map(int, input().split())

# top-down
count = 0
while(True):
    if A > B:
        count = -1
        break
    if A == B:
        count += 1
        break

    if B % 2 == 0:
        B = B // 2
        count += 1
    elif B % 10 == 1:
        B = B // 10
        count += 1
    else:
        count = -1
        break

print(count)

# BFS
q = deque()
q.append((A, 1))

while(q):
    a, cnt = q.popleft()

    if (a == B):
        print(cnt)
        break
    if (a > B):
        continue

    q.append((a * 2, cnt + 1))
    q.append((a * 10 + 1, cnt + 1))
else:
    print(-1)
