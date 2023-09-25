'''
1. X가 1이 될 때까지 연산을 사용하는 횟수의 최솟값
    3으로 나누어 떨어지거나, 2로 나누어 떨어지거나, 1을 뺀뒤에 2 or 3으로 나누어 떨어지거나
    시간재한 Python 3: 1.5 초
2. greedyX(10->9->3->1)
3. dn = min(dn, dn-1 + dn-2)
4. Propose a alternative solution
5. Implement the solution

7 -> 6, 3, 2
10 -> 
9= 8, 4, 3 
5= 4, 2, 
3

* operator // 결과는 내림
* dp 점화식을 위해 규칙을 생각해보지
* memoization 해야 시간초관 안난다
'''

# 시간초과
# X = int(input())

# def dp(x):
#     if x == 1:
#         return 0
#     elif x == 2 or x== 3:
#         return 1
#     else:
#         dpv = []
#         if x % 3 == 0:
#             dpv.append(dp(x//3))
#         if x % 2 == 0:
#             dpv.append(dp(x//2))
#         dpv.append(dp(x-1))
#         return min(dpv) + 1

# print(dp(X))

# Memoization
x = int(input())
dp = [0] * (x+1)

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[x])