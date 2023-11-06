'''
1. 0 < N <= M < 30, N개의 다리를 지을 수 있는 경우의 수
2. DP
3. table N x M : dp[i][j] = dp[i-1][j-1] + d[i][j-1]
4. 조합 mCn = m! / (m-n)!n!
5. Implement the solution
'''


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


T = int(input())

dp = [[0] * 30 for _ in range(30)]

for _ in range(T):
    N, M = map(int, input().split())
    print(factorial(M) // (factorial(N) * factorial(M-N)))

    print(dp[N][M])
