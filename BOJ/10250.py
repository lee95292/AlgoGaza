import sys
sys.stdin  = open("input.txt","r")

T = int(input())

for i in range(T):
    h,w,n = map(int,input().split())
    rn = n%h * 100 + n // h +1
    if rn < 100 :
        rn = rn + h * 100
    if n%h == 0 :
        rn =rn - 1
    print(rn)