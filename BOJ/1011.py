#import sys
#sys.stdin = open("input.txt","r")
T = int(input())
for k in range(T):
    a,b = map(int,input().split())
    r = 1
    for i in range(1000000):
        if b - a < i*i:
            r=i-1
            break
    ans = 2* r -1
    rest = b-a - r*r
    #print('r rest',r, rest)
    for j in range(r, 0,-1):
        if rest ==0:
            break
        if rest < j or rest < j* (rest // j):
            continue
        #print('k',j,rest, ans)
        ans = ans + rest // j
        rest = rest- j* (rest // j)
    print(ans)