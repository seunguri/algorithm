'''
1. 가장 큰 점수 차이로 우승하기 위해 n발의 화살을 어떤 과녁 점수에 맞혀야 하는지
2. DFS, 라이언이 맞힌 화살 개수 0 , info[i+1] 수행(점수O=info[i] + 1, 점수X=0)
    -> 경우의 수 = 2**11
3. 
    DFS
    - 0, info[i + 1] DFS 수행 
    - 어피치/라이언 점수 계산
    
    결과값 계산
    - 최대값이 여러개면 가장 낮은 점수를 더 많이 맞힌 경우
        - 남는 화살은 0점 맞추기
    - 라이언의 점수가 어피치의 점수보다 낮거나 같으면 [-1]
    
4. Propose a alternative solution
5. Implement the solution

reference:
화살 10개가 과녁 11개를 선택 ->
    중복조합 -> 11개 과녁 H 10개 화살 = 184756

    ** 중복조합 유도해보자
    서로 다른 과녁(3,4,6)을 구별하기 위해 기호를 넣으면?
    33446 -> 33|44|6
    기호를 먼저 그린 후 과녁을 채운다고 가정하면?
    7개 공간 중 칸막이 2개 선택 -> 과녁 3 종류 채워 넣음
    nHr = n+r-1Cr = n+r-1Cn-1
    3H5 = 7C5 = 7C2

'''

answer = [-1]
max_diff = 0

def isLower(ryan, answer):
    for i in range(10, 0, -1):
        if ryan[i] > answer[i]: return True
        elif ryan[i] < answer[i]: return False


def calc_score_diff(ryan, apeach):
    rscore = 0
    ascore = 0
    for i in range(11):
        if ryan[i] > apeach[i]: rscore += 10 - i
        elif apeach[i] > 0: ascore += 10 - i
    
    return rscore - ascore

def dfs(i, arrow, ryan, apeach):
    global max_diff, answer

    if arrow == 0 or i == 11:
        ryan[10] += arrow
        diff = calc_score_diff(ryan, apeach)
        if diff > 0 and diff >= max_diff:
            if max_diff == diff and isLower(ryan, answer): return
            max_diff = diff
            answer = ryan[:]
        ryan[10] -= arrow
        return
    
    if apeach[i] < arrow:
        ryan[i] += apeach[i] + 1
        dfs(i+1, arrow-apeach[i]-1, ryan, apeach)
        ryan[i] -= apeach[i] + 1

    dfs(i+1, arrow, ryan, apeach)


def solution(n, info):
    global answer

    dfs(0, n, [0]*11, info)
        
    return answer

print(solution(5,   [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1,	[1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9,	[0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10,	[0,0,0,0,0,0,0,0,3,4,3]))