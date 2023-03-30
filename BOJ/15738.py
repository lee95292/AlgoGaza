import sys
input = sys.stdin.readline
N,K,M = map(int,input().split())
arr = list(map(int,input().split()))
K-=1
for i in range(M):
    r = int(input())
    if r < 0 and K>=N+r :
        K = 2*N + r - K-1
    elif r > 0 and K <= r-1:
        K = r-1-K
print(K+1)