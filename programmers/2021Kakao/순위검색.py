from collections import defaultdict
from itertools import combinations

def solution(info, query):
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