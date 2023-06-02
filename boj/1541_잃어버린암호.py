# 음수가 커지고 양수가 작아져야 최소값이 된다.
# - 부호 다음 + 부호가 나오면 괄호를 넣고 - 부호가 나오면 넣지 않는다.
# 즉, - -> +이면 양수에서 뺄셈하는 쪽으로 더한다.

# eval() 사용 시 0009와 같이 int가 0으로 시작하면 SyntaxError다

expression = input()
result = 0

num_term = []
for epr in expression.split('-'):
    num_term.append(sum(map(int, epr.split('+'))))

result = num_term[0] - sum(num_term[1:])
print(result)