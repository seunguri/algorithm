'''
1. 0노드의 방문횟수가 최대인 수, 1노드방문횟수가 0과 같아지면 0방문횟수 초기화
2. DFS
3. 노드 최대 17개, O(n^2) 굳
    - 늑대가 양과 같아져도 다른 노드에 양이 몰려있을 수 있다.
    - 양의 수 > 늑대의 수?

    - 양이 연결되어 있으면 먼저 다 방문한다.
4. BFS는 경로의 특징을 기억하지 못한다
5. Implement the solution
'''

def solution(info, edges):
    visited = [0] * len(info)
    answer = 0

    def dfs(sheep, wolf):
        nonlocal answer
        if sheep > wolf: answer = max(answer, sheep)
        else: return

        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 0: dfs(sheep + 1, wolf)
                else: dfs(sheep, wolf + 1)
                visited[c] = 0
         
    visited[0] = 1
    dfs(1, 0)

    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],	[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0],	[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))
