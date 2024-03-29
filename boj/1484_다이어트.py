'''
1. Clarify the problem
    answer^2 - memory^2 = G
2. Define your approach
    G <= 100,000
    1 <= memory <= answer(더 쪘어 ㅠㅠ) <= 101
3. Propose a solution
    two pointer,
    - 현재 차 N >= G 또는 e == n, s++
    - 그렇지 않다면 e++
    - 현재 차가 G와 같다면 결과에 추가
4. Propose a alternative solution
5. Implement the solution
'''

def solution(G):
    results = []
    left = 1
    right = 2
    while True:
        if right ** 2 - (right-1)**2 > 100000:
            break
        if right ** 2 - left**2 < G:
            right +=1
            continue
        elif right ** 2 - left**2 >G:
            left +=1
            continue
        elif (right ** 2 - left**2) ==G:
            results.append(right)
            right += 1
            continue
    return sorted(results) if results else [-1]

G = int(input())

for weight in solution(G):
    print(weight)
