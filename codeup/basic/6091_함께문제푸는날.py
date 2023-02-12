'''
같은 날 동시에 가입한 3명의 사람들이 온라인 채점시스템에 들어와 문제를 푸는 날짜가
매우 규칙적이라고 할 때, 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?

예를 들어 3명이 같은 날 가입/등업하고, 각각 3일마다, 7일마다, 9일마다
한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 함께 문제를 풀게 된다.

갑자기 힌트?
왠지 어려워 보이지 않는가?
수학에서 배운 최소공배수를 생각한 사람들도 있을 것이다. 하지만, 정보에서 배우고 경험하는
정보과학의 세상은 때때로 컴퓨터의 힘을 빌려 간단한 방법으로 해결할 수 있게 한다.

문제 해석:
1. 브루트포스
2. 유클리드 호제법
'''

day = 1
user1, user2, user3 = map(int, input().split())
while day % user1 != 0 or day % user2 != 0 or day % user3 !=0:
    day += 1
print(day)
