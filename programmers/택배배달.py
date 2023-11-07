'''
1. n이 100000이므로 n^2, logn 안됌
2. greedy 최대 용량 택배 수용, 먼거리를 조금 가야함 → 가장 먼 집의 택배 배달,수거
3. 뒤에 집에서부터 cap을 빼면서 왕복거리 덧셈
4. Propose a alternative solution
5. Implement the solution
'''


def solution(cap, n, deliveries, pickups):
    answer = 0

    while True:
        far_n = -1
        d_cap = cap
        p_cap = cap

        for i in range(n, 0, -1):
            if deliveries[i-1] > 0:
                if i > far_n:
                    far_n = i
                box = min(d_cap, deliveries[i-1])
                d_cap -= box
                deliveries[i-1] -= box

            if pickups[i-1] > 0:
                if i > far_n:
                    far_n = i
                box = min(p_cap, pickups[i-1])
                p_cap -= box
                pickups[i-1] -= box

            if p_cap == 0 and d_cap == 0:
                break

        if far_n == -1:
            break
        else:
            answer += 2 * far_n

    return answer


cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]

print(solution(cap, n, deliveries, pickups))
