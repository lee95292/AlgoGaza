import sys
import math
sys.stdin = open('input.txt','r')

arr = [1 for i in range(0,123457*2)]
arr[0],arr[1] = 0,0
n =123457*2
end= int(math.sqrt(n))
for i in range(2, end+1):
    if arr[i] == 0:
        continue
    rm = arr[i*i:n+1:i]
    arr[i*i:n+1:i] = [0]*len(rm)
while True:
    n = int(input())
    if n == 0 :
        break

    print(sum(arr[n+1:2*n+1]))

