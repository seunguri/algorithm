attendance = [0] * 30
for _ in range(28):
    std = int(input())
    attendance[std - 1] = 1
for i, std in enumerate(attendance):
    if not std: print(i + 1)