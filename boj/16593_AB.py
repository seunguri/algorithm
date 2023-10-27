'''
1. A*2, A1 -> B가 되는 연산의 최솟값
2. greedy
3. B가 짝수면 2로 나누고 1이 끝에나오면 제거
4. bfs
5. Implement the solution
'''

A, B = map(int, input().split())
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
