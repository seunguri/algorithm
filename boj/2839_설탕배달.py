N = int(input())

result = N // 5 
N = N % 5
while N != 0:
    if result > 0:
        if N % 3 == 0:
            result += N // 3
            N = 0
        else:
            result -= 1
            N += 5
    else:
        if N % 3 == 0:
            result += N // 3
            N = 0
        break

if N == 0: print(result)
else: print(-1)