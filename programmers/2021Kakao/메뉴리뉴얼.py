from itertools import combinations
from collections import Counter

def solution_0(orders, course):
    answer = []
    for c in course:
        comb_list = []
        for order in orders:
            comb_list += list(combinations(sorted(order), c))
        count_dict = Counter(comb_list)
        
        for k, v in count_dict.items():
            if v >= 2 and v == max(count_dict.values()):
                answer.append("".join(k))
    
    return sorted(answer)

'''
1. Clarify the problem
    조합
2. Define your approach
    couse에 있는 단위로 각 orders 문자열을 쪼개서 count
3. Propose a solution
    dict에 부분문자열을 키, count를 값으로 함.
    2 이상이면 answer에 추가
    answer 정렬
4. Propose a alternative solution
5. Implement the solution
'''

def solution(orders, course):
    answer = []

    for i in range(len(orders)):
        orders[i] = "".join(sorted(orders[i]))

    for unit in course:
        candidate = dict()
        max_cnt = 0
        for order in orders:
            for sub in combinations(order, unit):
                menus="".join(sub)
                cnt = candidate.get(menus, 0) + 1
                candidate[menus] = cnt
                if max_cnt < cnt: max_cnt = cnt
        if max_cnt > 1:
            for m, c in candidate.items():
                if max_cnt == c:
                    answer.append(m)

    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))