# solutin with eval
abc = input()
exp = abc.replace(" ", "+")
print(eval(exp))

# solution with for loop
result = 0
for num in abc.split():
    result += int(num)
print(result)

# solution with sum
print(sum(map(int, abc.split())))