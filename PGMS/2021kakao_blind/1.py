def solution(new_id):
    new_id = new_id.lower()
    answer=''
    bf=''
    for i in new_id:
        if ord('0')<=ord(i)<=ord('9') or ord('a') <= ord(i) <=ord('z') or ord(i) in [ord('-'),ord('_'),ord('.')]:
            if bf == '.' and i == '.':
                continue
            answer += i
            bf = i
        
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[0:-1]
    if answer == '':
        answer += 'a'
    if len(answer) >=15:
        answer=answer[:15]
    if answer[-1] == '.':
        answer = answer[0:-1]

    if len(answer) <= 2:
        while len(answer) <=2:
            answer += answer[-1]
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution(	"=.="))
print(solution(	"123_.def"))
print(solution("z-+.^."))