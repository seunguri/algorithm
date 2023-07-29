# A＠B = (A+B)×(A-B)

def at(a, b):
    return (a + b) * (a - b)
a, b = map(int, input().split())
print(at(a, b))