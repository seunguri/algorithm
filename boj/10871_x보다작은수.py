n, x = map(int, input().split())
result = [ i for i in map(int, input().split()) if i < x]
print(*result)