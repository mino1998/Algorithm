# O(N^2) worst
#def solution(participant, completion):
#    for i in completion:
#        if i in participant:
#            participant.remove(i)
#    answer = participant[0]
#    return answer

def solution(participant, completion):
    hash_table = {}
    # 참가자들을 해시 테이블에 추가, 등장 횟수를 카운트합니다.
    for person in participant:
        hash_table[person] = hash_table.get(person, 0) + 1
    # 완주한 참가자들의 등장 횟수를 해시 테이블에서 감소시킵니다.
    for person in completion:
        hash_table[person] -= 1
    # 해시 테이블을 순회하며 등장 횟수가 1 이상인 참가자를 찾습니다.
    for person in hash_table:
        if hash_table[person] > 0:
            return person