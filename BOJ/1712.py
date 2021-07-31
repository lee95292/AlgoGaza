import sys
import math

sys.stdin = open("input.txt", "r")

a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    x= math.ceil(a/(c-b))
    if x == a/(c-b):
        x =x+1
    print(x)
