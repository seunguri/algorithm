N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)

S = sum([a * b for a, b in zip(A, B)])
print(S)