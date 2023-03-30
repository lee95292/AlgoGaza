import sys
input = sys.stdin.readline

N = int(input())
tnt = []

for i in range(N):
    tnt.append(int(input()))

if len(tnt) == 1:
    print(1)
    exit(0)

flow = tnt[1] - tnt[0] 
if flow < 0 : 
    print(1)
answer = 0
for i in range(0,N-1):
    if flow >= 0 and  tnt[i] >= tnt[i+1]:
        print(i+1)
    flow = tnt[i+1] - tnt[i]
    
if flow >= 0:
    print(N)