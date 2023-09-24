메모리를 사용하여 하나의 문제를 단 한 번만 풀도록 하는 알고리즘

1. Optimal SubstructureThe big problem can be divided into small problems, and the answer to the small problem can be gathered to solve the big problem.
2. **Overlapping Subproblem**
   The same small problem needs to be solved repeatedly.

피보나치 수열을 재귀 함수로 해결하면 지수 시간 복잡도 O(2^N)를 가진다. -> 중복되는 부분 문제 - memoization하면 O(N)
LIS(Longest Increasing Subsequence)

### Top down

- Memoization
- caching

### Bottom up

- DP table

# 주어진 문제가 DP 유형임을 파악하자

1. 그리디, 구현, 완전 탐색 등의 아이디어로 문제를 해결할 수 있는지 검토
2. 다른 알고리즘으로 풀이 방법이 떠오르지 않으면 DP 고려
   - 작은 문제로 큰 문제 해결(optimal substructure) + 부분 문제 중복(overlapping subproblem)
3. 재귀 함수로 비효율적인 완전 탐색 프로그램을 작성
4. 작은 문제에서 구한 답이 큰 문제에 그대로 사용될 수 있으면, 메모이제이션으로 코드 개선 가능
