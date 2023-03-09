"""
문제: https://www.acmicpc.net/problem/5585
풀이: 모든 거스름돈의 단위가 500엔의 약수이므로 무조건 금액이 큰 거스름돈부터 지급한다.
"""

price = 1000 - int(input())
count = 0

count += price // 500
price %= 500
count += price // 100
price %= 100
count += price // 50
price %= 50
count += price // 10
price %= 10
count += price // 5
price %= 5
count += price

print(count)
