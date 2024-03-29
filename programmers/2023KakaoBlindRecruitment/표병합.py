'''
1. - merge란 같은 값을 공유
    근거: 선택한 두 셀은 서로 인접하지 않을 수도 있다. 그 사이의 위치한 셀들은 영향X
   - 값이 없어도 병합 가능
    근거: unmerge시 해당 셀의 모든 병합을 해제

2. 어떤 자료구조를 사용할까? [value, [(r, c), (r2, c2), ...]]
    근거: 
        - merge 정의에 따라 병합은 데이터의 공유이므로 value를 셀마다 일일이 저장할 필요없다.
         각각의 value에 셀 정보를 저장한다
        - unmerge command를 위해서 병합된 셀 끼리의 정보가 필요하다
        - 같은 value지만 병합은 아닐 수 있다
    이점: 
        - update value1 value2 에서 value 값만 바꾸면 모든 셀이 업데이트 됨
3. Propose a solution
4. Propose a alternative solution
5. Implement the solution
'''


def solution(commands):
    answer = []

    values = []

    def findv(target):
        for i in range(len(values)):
            if values[i][0] == target:
                return i
        return -1

    def findrc(r, c):
        for i in range(len(values)):
            for p in values[i][1]:
                if p[0] == r and p[1] == c:
                    return i
        return -1

    for command in commands:
        token = command.split()
        if token[0] == "UPDATE":
            if len(token) > 3:
                idx = findrc(token[1], token[2])
                if idx > -1:
                    values[idx][0] = token[3]
                else:
                    values.append([token[3], [(token[1], token[2])]])
            else:
                idx = findv(token[1])
                if idx > -1:
                    values[idx][0] = token[2]

        elif token[0] == "MERGE":
            if token[1] == token[3] and token[2] == token[4]:
                continue
            idx1 = findrc(token[1], token[2])
            idx2 = findrc(token[3], token[4])
            if idx1 != idx2 or idx1 == -1:
                if idx1 > -1:
                    if idx2 > -1:
                        if len(values[idx1][0]) < 1:
                            values[idx2][1].extend(values[idx1][1][:])
                            del values[idx1]
                        else:
                            values[idx1][1].extend(values[idx2][1][:])
                            del values[idx2]
                    else:
                        values[idx1][1].append((token[3], token[4]))
                elif idx1 < 0 and idx2 > -1:
                    values[idx2][1].append((token[1], token[2]))
                elif idx1 < 0 and idx2 < 0:
                    values.append([
                        "", [(token[1], token[2]), (token[3], token[4])]])

        elif token[0] == "UNMERGE":
            idx = findrc(token[1], token[2])
            if idx > -1:
                values[idx][1] = [(token[1], token[2])]

        elif token[0] == "PRINT":
            idx = findrc(token[1], token[2])
            v = "EMPTY"
            if idx > -1:
                v = values[idx][0]
            answer.append(v)

    return answer


# print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant",
#      "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
# print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d",
#      "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))
# print(solution(["MERGE 1 1 1 2", "UPDATE 1 3 A",
#      "MERGE 1 1 1 3", "UNMERGE 1 2", "PRINT 1 2"])) # r1, c1 "" 인 경우 r2c2 에 병합 반례
print(solution(["UPDATE 4 1 pasta", "UPDATE 4 3 pasta",
      "MERGE 4 2 4 2", "UNMERGE 4 1", "UPDATE italian italian", "PRINT 4 2"]))
