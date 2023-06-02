# 돈을 인출하는데 필요한 시간의 합은 무조건 인출시간이 짧은 사람부터 줄을 서면 된다.
# 왜냐하면 인출시간의 합은 N명일 때, (N*P1 + (N-1)*P2 + ... + PN) 이기 때문이다.

from functools import reduce

N = int(input())
P = list(map(int, input().split()))

P.sort()
result = reduce(lambda x, y: x + y, map(lambda x, y: x * y, P, range(N, 0, -1)))
print(result)