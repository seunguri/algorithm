'''
1. summurize [a-1][0]~[a-1][b-1], [0][i] => i
2. DP Memoization
3. Propose a solution
4. Propose a alternative solution
5. Implement the solution
'''

T = int(input())
floor = []
room = []
for _ in range(T):
    floor.append(int(input()))
    room.append(int(input()))

apartment = [[i + 1 for i in range(max(room))]]
for i in range(1, max(floor)+1):
    f = []
    for j in range(len(apartment[0])):
        f.append(sum(apartment[i-1][0:j+1]))
    apartment.append(f)

for i in range(T):
    print(apartment[floor[i]][room[i]-1])