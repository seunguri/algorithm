'''
격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,
격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

입력
첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
두 번째 줄에 놓을 수 있는 막대의 개수(n)
세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.
1 <= w, h <= 100
1 <= n <= 10
d = 0 or 1
1 <= x <= 100-h
1 <= y <= 100-w

문제 해석:
2차원 배열
'''

h, w = map(int, input().split())
n = int(input())
board = [[0] * w for _ in range(h)]  # 빈 바둑판
for i in range(n):  # 바둑판에 막대 놓기
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:
            board[x - 1][y - 1 + j] = 1
        else:
            board[x - 1 + j][y - 1] = 1

for i in range(h):
    for j in range(w):
        print(board[i][j], end=' ')
    print()
