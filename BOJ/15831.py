"""
15841 투포인터

10 0 1
BWBWBWBWBW
"""
import sys
input = sys.stdin.readline
N, B, W = map(int, input().split())
S = input()
l,r = 0, -1
rockCnt= {'B':0, 'W':0}
answer = 0

for l in range(N):
    while r+1 < N and (S[r+1] == 'W' or rockCnt['B'] < B ):
        r+=1
        rockCnt[S[r]]+=1
    if rockCnt['W'] >= W:
        answer = max(answer, rockCnt['W']+rockCnt['B'])
    # print(rockCnt, l,r)
    rockCnt[S[l]]-=1
    
print(answer)

