'''
1. 1서비스 가입자, 2판매액을 최대로
    할인을 너무 많이 하면, 가입자가 적음
    할인을 너무 조금 하면, 가입자는 동일해도 매출액이 적을 수 있음
    할인율: 10, 20, 30, 40
    이모티콘 마다 할인율이 다를 수 있음

    n명이 특정 할인율 이상인 m개의 이모티콘 구매, 특정 가격이 넘으면 서비스 가입
    1 <= n <= 100
    1 <= m <= 7

    모든 할인을 모든 사람에게 적용하는 시간 복잡도 -> O(4nm)

2. Define your approach
    재귀로 모든 경우를 모두 확인
    가입자가 가장 많은 이모티콘 별 할인율을 찾는다. -> 할인율별 총 가격을 구한다 -> (4 * n) * (4 * m)개
    가입자 개수가 동일한 값이 여러개라면 이익이 더 많은 값을 선택

3. Propose a solution
4. Propose a alternative solution
5. Implement the solution
'''


def solution(users, emoticons):
    answer = [0, 0]
    ratios = [10, 20, 30, 40]
    discounts = []

    def dfs(discount):
        if len(discount) == len(emoticons):
            discounts.append(discount[:])
            return

        for ratio in ratios:
            discount.append(ratio)
            dfs(discount)
            discount.pop()
    dfs([])

    for discount in discounts:
        join = 0
        profit = 0
        for user in users:
            price = 0
            for i in range(len(discount)):
                if user[0] > discount[i]:
                    continue
                price += emoticons[i]//100 * (100 - discount[i])
            if price >= user[1]:
                join += 1
            else:
                profit += price

        if answer[0] < join or (answer[0] == join and answer[1] < profit):
            answer[0] = join
            answer[1] = profit

    return answer


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [
      40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
