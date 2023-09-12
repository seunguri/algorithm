"""
무조건 큰 시간 단위의 버튼을 우선 누르고 나머지를 다음 크기의 버튼을 누른다.
풀이1. 초단위로 변경 후 A부터 나머지가 0이 될때까지 나눈다. O(N)
풀이2. T초를 분단위로 나누고 쪼갠다 O(1)
"""

T = int(input())
if T % 10 != 0:
    print(-1)
else:
    minute = T // 60
    second = T % 60
    print(minute // 5, minute % 5, second // 10)
