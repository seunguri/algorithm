'''
1. Clarify the problem
    설치/삭제 조건 여부 판단
2. Define your approach
    - 기둥, 보 설치 조건
    - 설치된 구조물 정보
    - 위 두 요소를 바탕으로 건설/무시 판단
3. Propose a solution
    - 조건을 어떻게 판단할 것 인가
        구현
        구조물은 교차점 좌표를 기준으로 보는 오른쪽, 기둥은 위쪽 방향으로 설치 또는 삭제합니다.
        기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
        보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
    
    - 예외처리 안해도 되는 경우
        벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다.
        바닥에 보를 설치 하는 경우는 없습니다.
        구조물이 겹치도록 설치하는 경우와, 없는 구조물을 삭제하는 경우는 입력으로 주어지지 않습니다.

    x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다.
4. Propose a alternative solution
5. Implement the solution
'''
# x, y 좌표에 있는 기둥이 적절한가
def check_pillar(pillar, beam, x, y):
    if y == 0: return True
    if pillar[x][y-1] == 1: return True
    if beam[x-1][y] == 1 or beam[x][y] == 1: return True 
    
    return False

# x, y 좌표에 있는 보가 적절한가
def check_beam(pillar, beam, x, y):
    if pillar[x][y-1] == 1 or pillar[x+1][y-1] == 1: return True 
    if beam[x-1][y] == 1 and beam[x+1][y] == 1: return True

    return 

def solution_fail(n, frame):
    pillar = [[0] * (n+2) for _ in range(n+1)]
    beam = [[0] * (n+2) for _ in range(n+1)]

    for x, y, a, b in frame:
        check = False
        if a == 0: # 기둥
            if b == 0: # 삭제
                pillar[x][y] = 0
                if not check_pillar(pillar, beam, x, y+1) or not check_beam(pillar, beam, x, y+1) or not check_beam(pillar, beam, x-1, y+1): 
                    pillar[x][y] = 1
            else: # 설치
                if check_pillar(pillar, beam, x, y): pillar[x][y] = 1
            
        else: # 보
            if b == 0: # 삭제
                beam[x][y] = 0
                if not check_pillar(pillar, beam, x, y) or not check_pillar(pillar, beam, x+1, y) or not check_beam(pillar, beam, x-1, y) or not check_beam(pillar, beam, x+1, y):
                    beam[x][y] = 1
            else: # 설치
                if check_beam(pillar, beam, x, y): beam[x][y] = 1

    answer = []
    for i in range(n+1):
        for j in range(n+1):
            if pillar[i][j] == 1: answer.append([i, j, 0])
            if beam[i][j] == 1: answer.append([i, j, 1])

    return answer

def check_build(answer):
    for x, y, a in answer:
        # 기둥
        if a == 0:
            if (y != 0 and
                [x, y - 1, 0] not in answer and
                [x - 1, y, 1] not in answer and
                [x, y, 1] not in answer):
                return False
        # 보
        else:
            if ([x, y - 1, 0] not in answer and
                [x + 1, y - 1, 0] not in answer and
                ([x - 1, y, 1] not in answer or
                 [x + 1, y, 1] not in answer)):
                return False
    return True
 
def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 0:
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])
        elif b == 1:
            answer.append([x, y , a])
            if not check(answer):
                answer.remove([x, y, a])
 
    answer.sort(key= lambda x : (x[0], x[1], x[2]))
    return answer
print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))