import sys
#sys.stdin = open('input.txt','r')

import math
m,n = map(int,input().split())

arr = [i for i in range(0,1000002)]
end= int(math.sqrt(n))
for i in range(2, end+1):
    if arr[i] == 0:
        continue
    rm = arr[i*i:n+1:i]
    arr[i*i:n+1:i] = [0]*len(rm)
#    for j in range(i*i, n+1):
#        if j % i == 0:
#            arr[j] = 0
#for i in range(2,j):

#print(arr[0:30])
for i in arr[m:n+1]:
    if i!= 0 and i != 1:
        sys.stdout.write(str(i) + '\n')
