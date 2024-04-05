from collections import defaultdict
from itertools import combinations

def solution_0(info, query):
    answer = []

    info_hash = defaultdict(list)

    for i in info:
        splited_info = i.split()
        score = splited_info.pop()
        for r in range(5):
            combs = combinations(range(4), r)

            for comb in combs:
                key = splited_info[:]
                for elem in comb:
                    key[elem] = "-"

                info_hash[" ".join(key)].append(int(score))

    for item in info_hash:
        info_hash[item].sort()

    for q in query:
        splited_q = q.replace(" and", "").split()
        target_score = int(splited_q.pop())

        target_key = " ".join(splited_q)

        matched_score_list = info_hash[target_key]
		
        if not matched_score_list:
            answer.append(0)
            continue

        score_len = len(matched_score_list)
		
        #upper bound 알고리즘
        start = 0
        end = score_len
        mid = (start + end) // 2

        while start < end:
            mid = (start + end) // 2

            mid_score = matched_score_list[mid]

            if mid_score < target_score:
                start = mid + 1

            else:
                end = mid

        answer.append(score_len - start)

    return answer

'''
1. Clarify the problem
    - info 개수: 1~50,000
    - query 개수: 1~100,000
2. Define your approach
    - 조건마다 info index -> query 
    - query 교집합
3. Propose a solution
    - 조건 key, info value
4. Propose a alternative solution
5. Implement the solution
'''

def solution_0(info, query):
    answer = []
    score = []
    condition = {}
    score = {}

    for i in range(len(info)):
        con = info[i].split(" ")
        for j in range(3):
            condition[con[j]].append(i)
        ss = score.get(con[3], [])
        ss.append(i)

    return answer

from bisect import bisect_left
from collections import defaultdict
from itertools import combinations

def solution(info, query):
    answer = []
    dic = {}
    comb = [0, 1, 2, 3]
    for i in info:
        person = i.split()
        conditions = person[:-1]
        score = int(person[-1])
        for j in range(5):
            for k in list(combinations(comb, j)):
                temp = conditions.copy()
                for idx in k:
                    temp[idx] = '-'
                key = ''.join(temp)
                if key in dic:
                    dic[key].append(score)
                else:
                    dic[key] = [score]
    
    for value in dic.values():  
        value.sort()

    for i in query:
        q_list = []
        for j in i.split():
            if j == 'and':
                continue
            q_list.append(j)

        target = int(q_list[-1])
        key = ''.join(q_list[:-1])

        if key in dic:
            hubo_list = dic[key]

            index = bisect_left(hubo_list, target)
            answer.append(len(hubo_list) - index)
        else:
            answer.append(0)
            continue

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))