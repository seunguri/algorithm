def cert(nums):
    return sum(nums ** 2) % 10

print(sum([n**2 for n in map(int, input().split())]) % 10)