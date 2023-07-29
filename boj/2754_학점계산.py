grade = input()
result = 0.0
if grade[0] == 'A':
    result += 4.0
elif grade[0] == 'B':
    result += 3.0
elif grade[0] == 'C':
    result += 2.0
elif grade[0] == 'D':
    result += 1.0

if result != 0.0:
    if grade[1] == '+':
        result += 0.3
    elif grade[1] == '-':
        result -= 0.3
print(result)