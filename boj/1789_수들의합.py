'''
최대한 많은 수(N)를 더해서 S를 만든다.
1+2+3+4+..=S 가 최대한 많은 수 N의 경우이다.
'''

S = int(input())
N = 0
sum_n = 0
for i in range(1, S+1):
    sum_n += i
    N = i
    if sum_n > S:
        N -= 1
        break
print(N)
