import  sys
import heapq
input = sys.stdin.readline

v,e = list(map(int,input().split()))
st = int(input())

graph = [ [] for _ in range(v+1)]
dist = [0-1]*(n+1)

for i in range(e):
    a,b,f = list(map(int,input().split()))


que = []
heapq.heappush(st)


"""
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
"""