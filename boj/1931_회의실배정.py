t = int(input())
time_table = []
for _ in range(t):
    time_table += tuple(map(int, sys.stdin.readline().split()))
time_table.sort()

result = 0
for i in time_table[-1][0]:
    j = 0
    count = 0
    for s, e in time_table:
        if s >= j:
            if e <= i:
                count += 1
                j = e
            else:
                continue
        else:
            break