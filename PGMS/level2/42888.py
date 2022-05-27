"""
오픈채팅방
"""

def solution(record):
    answer = []
    id_name = {}
    for rec in record:
        log = rec.split()

        if log[0] == 'Enter':
            id_name[log[1]] = log[2]
            answer.append(log[1]+'님이 들어왔습니다.')
        elif log[0] == 'Leave':
            answer.append(log[1]+'님이 나갔습니다.')
        elif log[0] == 'Change':
            id_name[log[1]] = log[2]

    for idx,ans in enumerate(answer):
        #print(ans.index('님'))
        id = ans[0:ans.index('님')]
        answer[idx] = id_name[id]+ans[ans.index('님'):]
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))