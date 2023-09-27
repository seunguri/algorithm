'''
1. 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수
    |       |
    |_______| 2
    1<= n <= 1000

    time: 1s
    memory: 256MB
    output: % 10007

2. DP
    2xn-1 직사각형으로부터 2xn직사각형을 구할 수 있음
    - obtimal substructure
    - overlapping subproblem
    
3. Propose a solution
    dn = (2 * dn-1) + (dn-2 + 1)
    - n-1의 경우 1x2 직사각형 1개를 사용
    - n-2의 경우 2x1 직사각형을 2개 사용
    - 2xn이므로 직사각형을 추가할 수 있는 방법은 나란히 놓는 방법만 존재함 -> || =

    n = 3
    - n = 2
        || + 1(|)
        = + 1(|)
    - n = 1
        | + 1(=)

4. Propose a alternative solution
5. Implement the solution
'''

n = int(input())
cache = [0] * 1001
cache[1] = 1
cache[2] = 2

for i in range(3, n+1):
    cache[i] = (cache[i-1] + cache[i-2]) % 10007

print(cache[n])

