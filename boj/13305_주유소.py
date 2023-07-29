"""
아이디어: 기름값이 비싼 주유소에서는 주유를 최소 또는 하지 않으며 싼 주유소에서는 최대로 주유한다.
구현:
1. 기름값이 최소인 주유소부터 제일 오른쪽 도시까지의 거리만큼 기름을 주유한다.
2. 남은 거리에서 1번의 거리을 제외한다.
3. 1번 주유소 이후에 있는 주유소는 제외한다.
4. 다음으로 기름값이 저렴한 왼쪽 길의 주유소에서 1,2,3을 반복한다.

코드 구현하다보니 위 순서 그대로 나오지 않음
* 맨뒤주유소는 이용하지 않고 맨앞주유소는 무조건 이용한다.
-> 2개의 리스트, 최소생각하다보니 반쪽짜리 2차원배열이 떠올라 구현했다.
"""

N = int(input())
distance_list = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

# result = 0
# for i in range(N - 1):
#     min = oil_price[i] * distance_list[i]
#     for j in range(1, i + 1):
#         price = oil_price[j] * distance_list[i]
#         if price < min:
#             min = price
#     result += min
# print(result)

# min_price = oil_price[0]
# result = min_price * distance_list[0]
# for i, distance in enumerate(distance_list[1:]):
#     if oil_price[i+1] < oil_price[i]:
#         min_price = oil_price[i+1]
#     result += min_price * distance
# print(result)

result = sum(distance_list) * oil_price[0]
min = oil_price[0]
for i in range(1, N - 1):
    if min > oil_price[i]:
        sub = min - oil_price[i]
        min = oil_price[i]
        result -= sum(distance_list[i:N - 1]) * sub
print(result)
