import math


def solution(brown, red):
    def quadratic_eq(a, b, c):
        return [(-b+math.sqrt(b*b-4*a*c))/2*a, (-b-math.sqrt(b*b-4*a*c))/2*a]

    return [int(x) for x in quadratic_eq(1, -2-brown/2, brown+red)]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
