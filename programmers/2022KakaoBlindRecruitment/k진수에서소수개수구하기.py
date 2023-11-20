'''
1. k진수 변환 -> **0으로 분할** -> 소수
2. k진수 변환 : 나머지를 문자열로 순서 거꾸로 합치기
    소수: 1과 자기 자신 만을 약수로 가지는 수
        1) 시간복잡도 O(n)
        for i in range(2, n):
            if num % i == 0: return false

        2) 시간복잡도 O(n**0.5) -> 약수의 중간값
        for i in range(2, int(n**0.5+1)):
            if(num % i == 0) return false

        3) 에라토스테네스의 체
        nums = [True for i in range(n+1)]
        for i in range(2, int(n**0.5+1)):
            if array[i] == True: 
                j = 2
                while i * j <= n:
                    array[i*j] = False
                    j += 1
3. 0으로 분할
4. Propose a alternative solution
5. Implement the solution
'''


def solution(n, k):
    answer = 0
    
    # k진수 변환
    kn = ""
    while n > 0:
        kn = str(n % k) + kn
        n = n // k

    # 0으로 분할
    for s in kn.split('0'):
        # 소수 확인
        if len(s) == 0: continue
        if int(s) < 2: continue
        is_prime = True
        for i in range(2, int(int(s)**0.5 + 1)):
            if int(s) % i == 0:
                is_prime = False
                break
        if is_prime: answer += 1
    
    return answer

print(solution(437674, 3))