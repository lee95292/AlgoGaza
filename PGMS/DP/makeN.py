# Colloboration[k]는 N을 k회 사용하여 만들 수 있는 수의 집합

import math


def solution(N, number):
    answer = 0
    combination = [[0], [N]]
    if(N == number):
        return 1

    for turn in range(2, 9):
        tmpCombination = []

        def extendNumber(n):
            for i in n:
                if(i < 1 or i > 32000):
                    continue
                tmpCombination.append(i)
        for r in range(1, math.floor(turn/2)+1):
            for k in combination[turn-r]:
                for s in combination[r]:
                    big = s
                    small = k
                    if(big < small):
                        big, small = small, big
                    klist = [small+big, small*big,
                             math.floor(big/small), big-small]
                    # if(number in klist):
                    #     return turn

                    extendNumber(klist)

        nn = int(str(N)*turn)

        if(nn < 32001):
            tmpCombination.append(nn)

        tmpCombination = list(set(tmpCombination))
        combination.append(tmpCombination)
        if(number in tmpCombination):
            return turn
        # print(str(turn)+":")
        # print(combination)
    return -1


print(solution(8, 88))
