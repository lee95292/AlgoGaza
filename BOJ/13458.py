"""
백준 13458 시험감독
5
1000000 1000000 1000000 1000000 1000000
5 7
"""
import math
N = int(input())
appliers = list(map(int,input().split()))
A,B = map(int,input().split())
answer = 0
for nApplier in appliers:
    if nApplier - A >= 0:
        answer += math.ceil((nApplier - A)/B)
    answer +=1
    
print(answer)