'''
1. 수를 섞어서 만들 수 있는 가장 큰 30의 배수
2. 10과 3의 공배수, 가장 큰 수 -> Greedy
3. 1) 0이 있는가 2) 3의 배수 판정
4. Propose a alternative solution
5. Implement the solution

[배수판정법]
https://ko.wikipedia.org/wiki/%EB%B0%B0%EC%88%98_%ED%8C%90%EC%A0%95%EB%B2%95
3의 배수: 각 자리 수의 합이 3의 배수인 수이다.
'''

N = input()

if "0" not in N:
    print(-1)
else:
    result = 0
    for i in range(len(N)):
        result += int(N[i])

    if result % 3 != 0:
        print(-1)
    else:
        sorted_N = sorted(N, reverse=True)
        result = "".join(sorted_N)
        print(result)
