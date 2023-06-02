N, K = map(int, input().split())
value_list = list()
for _ in range(N):
    value_list.append(int(input()))

result = 0
value_list.sort(reverse=True)
for value in value_list:
    # 만약 작은 가치의 동전 여러 개를 사용하였을 때 최솟값의 결과가 나올 수 있는가?
    # 동전의 가치를 조합했을 때 K원으로 나누어 떨어지지 않을 수 있는가?
    if value <= K:
        count = K // value
        result += count
        K -= value * count
        if K <= 0: break

print(result)

