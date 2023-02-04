"""
3
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8
5
2 5 4 5 3
"""
import sys
sys.setrecursionlimit(10**6+1)

T = int(input())

for tc in range(T):
    N = int(input())
    students = list(map(lambda x: int(x)-1,input().split()))
    