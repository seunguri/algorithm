'''
1. n을 1, 2, 3의 합으로 나타내는 방법의 수
    n: 1~10 
    time: 1s

    1+1+1+1
    1+1+2
    1+2+1
    2+1+1
    2+2
    1+3
    3+1
    -> 위치 중복
2. DP
3. optimal substructure + overlapping subproblem
    => (1,2,3)을 각각 뺀 n-(1,2,3)을 더합 합의 방법을 전부 합산한 값이다
4. DFS
5. Implement the solution
'''

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = sum(dp[i-3:i])
    
T = int(input())
for _ in range(T):
    print(dp[int(input())])
