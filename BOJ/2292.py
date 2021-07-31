import sys
#sys.stdin = open("input.txt","r")
import math

n =int(input())

cur = 1
val = 1
while val < n :
    val = 6 * cur + val
    cur+=1


print(cur)