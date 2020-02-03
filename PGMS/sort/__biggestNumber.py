def solution(numbers):
    answer = []
    numbers = sorted(numbers, key=lambda a: str(a)[0])
    snumbers = [str(a) for a in numbers]

    for n in range(0, len(numbers)):
        inst = 0
        ns = snumbers[n]
        for a in range(0, len(answer)):  # 이진탐색으로 수정하기
            ast = answer[a]
            if(ns[0] < ast[0]):
                continue
            elif(ns[0] > ast[0]):
                inst = 1
                answer.insert(a, ns)
                break
            elif(ns+ast > ast+ns):
                inst = 1
                answer.insert(a, ns)
                break
        if(inst == 0):
            answer.append(ns)
    return ''.join(answer)


print(solution([3, 30, 34, 5, 9]))
print(solution([6, 10, 2]))
