N = int(input())
int_map = map(int, input().split())
v = int(input())

count = 0
for i in int_map:
    if i == v: count += 1
print(count)