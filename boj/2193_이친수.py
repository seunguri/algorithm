'''
1. 0 맨앞x, 11 부분문자열 x인 N자리 문자열 개수
2. N = 3, _ _ _ 에서 위의 조건에 따라 1 0 _ 은 고정이고 마지막 _ 은 0 또는 1이므로 답은 2
   N = 4, 2 * 1 + 1
   N = 5, 2 * 2 + 1
   N = 6, 2 * 3 + 2
   N = 7, 2 * 5 + 3
   이고 이를 재귀식으로 나타내면 N = i, dp = 2 * dp(i-2) + dp(i-3)
3. Propose a solution
4. Propose a alternative solution
5. Implement the solution
'''

N = int(input())
dp = [0] * 91
dp[1] = 1
dp[2] = 1

if N > 2:
    for i in range(3, N + 1):
        dp[i] = dp[i-2]*2 + dp[i-3]
print(dp[N])
