'''
1. Clarify the problem: 
    총합, queue pop insert 횟수
    300000 size queue sum O(N)
2. Define your approach
    총합/2 -> 목표값
    목표보다 큰 큐에서 수행: 언젠가 L을 감소시키고 R을 증가시켜야 하고, 결국 queue1의 원소를 queue2로 넘겨주는 동작은 반드시 필요
3. Propose a solution
4. Propose a alternative solution: 투 포인터
5. Implement the solution
'''
from collections import deque

def solution_greedy(queue1, queue2):
    s1 = sum(queue1)
    s2 = sum(queue2)
    goal = (s1 + s2) // 2
    q1,q2 = deque(queue1), deque(queue2)

    i = 0
    for i in range(4*len(q1)):
        if s1 > s2:
            n = q1.popleft()
            s1 -= n
            s2 += n
            q2.append(n)
        elif s1 < s2:
            n = q2.popleft()
            s2 -= n
            s1 += n
            q1.append(n)
        else:
            return i

    return -1
    
# two pointer
def solution(queue1, queue2):
    goal = (sum(queue1) + sum(queue2)) // 2


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))	#2
print(solution([1, 2, 1, 2],	[1, 10, 1, 2]))	#7
print(solution([1, 1],	[1, 5]))	#-1