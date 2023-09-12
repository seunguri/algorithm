"""
풀이1. 오름차순으로 정렬 후 앞에서 부터 2개씩 더하기  O(2n)
풀이2. N개 합 +  N-1개 합 + N-2개 합 + 2개 합  O(2n)
    => 오름차순 정렬했을 때: i0^(N-1) + i1^(N-1) + i2^(N-2) + i^3(N-3) + ... iN^(N-N)

ref:https://hongjw1938.tistory.com/22
① 배열에 데이터 저장을 하고 새로 삽입할 때마다 서로 비교하면서 정렬해주면 되는 것 아닌가?
▶ 그런데 이 방식은 그다지 효율적이지 못하다. 왜냐하면 선형으로 처음부터 비교를 하면서 해당 자료를 삽입할 위치를 찾아야 하기 때문에 O(n)의 시간이 소요되고 n이 충분히 크다면 원하는 시간 안에 해결하기 어려울 수 있다.
 
② 그럼 배열에 저장하되, 퀵 정렬, 이진 탐색 같은 방식을 이용하면 훨씬 빠르게 삽입 / 추출 / 탐색도 가능하지 않은가?
▶ 맞다. 우선순위 큐는 그러한 방식을 하나의 자료구조로써 구현한 것이라고 보면 된다. 그것을 힙(Heap) 이라고도 부른다. 실제로 O(logn) 수준의 시간 복잡도를 유지한다.

"""

N = int(input())
# O(N)
# card_nums = [int(input()) for _ in range(N)]
# card_nums.sort()
# result = card_nums[0] * (N-1)
# for i in card_nums[1:]:
#     N -= 1
#     result += i * N

# O(logn)
from queue import PriorityQueue
que = PriorityQueue()
for _ in range(N):
    que.put(int(input()))
result = 0

if que.qsize == 1:
    print(result)
else:
    for _ in range(N-1):
        prev = que.get()
        curr = que. get()
        result += prev + curr
        que.put(prev + curr)
print(result)
