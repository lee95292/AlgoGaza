def solution(numbers):
    if(sum(numbers) == 0):
        return '0'

    answer = []
    numbers = sorted(numbers, key=lambda a: str(a)[0])
    snumbers = [str(a) for a in numbers]

    ln = len(numbers)
    for n in range(0, ln):
        inst = 0
        ns = snumbers[n]
        la = len(answer)
        st = 0
        if(ln < 2*la):
            if(answer[a//2] + snumbers[n] < snumbers[n]+answer[a//2]):
                st = a//2

        for a in range(st, la):  # 이진탐색으로 수정하기
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
print(solution([21, 212]))
print(solution([0, 0, 1000, 0]))


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
