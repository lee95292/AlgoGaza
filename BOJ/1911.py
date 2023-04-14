import math
import sys
input = sys.stdin.readline
N,L = map(int,input().split())

pools =[]
answer=0
coverLoc = 0
for i in range(N):
    pools.append(list(map(int,input().split())))

pools.sort(key = lambda x: x[0])
for a,b in pools:
    if a >= coverLoc: 
        coverLoc = a+ L* math.ceil((b-a)/L)
        answer += math.ceil((b-a)/L)
    else:
        k = math.ceil((b-coverLoc)/L)
        coverLoc += L* k
        answer += k
    # print(a,b,coverLoc)

print(answer)