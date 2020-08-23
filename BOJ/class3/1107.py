strTo = input()
to = int(strTo)
na = int(input())

if(na > 0):
    breaks = list(input().split())
else:
    breaks = []


def isReachable(num):
    for i in breaks:
        if(str(num).count(i) > 0):
            return False
    return True


def answer():
    res = abs(100-to)

    if(10 == na):
        return res
    for i in range(0, 500000):
        m, n = to+i, to-i
        if(isReachable(m)):
            res = min(m-to+len(str(m)), res)
        if(isReachable(n) and n >= 0):
            res = min(to-n+len(str(n)), res)
    return res


print(answer())

# strTo = input()
# to = int(strTo)
# na = int(input())
# breaks = list(input().split())


# def isReachable(num):
#     for i in breaks:
#         if(str(num).count(i) > 0):
#             return False
#     return True


# def answer():
#     if(10 == na):
#         return abs(100-to)
#     for i in range(0, 500000):
#         m, n = to+i, to-i
#         if(n < 0):
#             return abs(100-to)
#         if(isReachable(m)):
#             return min(m-to+len(str(to)), abs(100-to))
#         if(isReachable(n)):
#             return min(to-n+len(str(to)), abs(100-to))


# print(answer())
