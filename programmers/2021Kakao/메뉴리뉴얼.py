from itertools import combinations
from collections import Counter

def solution(orders, course):
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