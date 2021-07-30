#import sys
#sys.stdin = open("input.txt", "r")

n = int(input())
arr = [] # 정답 순여
asc = [x for x in range(1,n+1)]
stack = []
dest = []
sol = []
for i in range(n):
    arr.append(int(input()))

flag = True
while len(dest) != n:
    if len(stack) == 0 or arr[0] != stack[-1]:
        if len(asc) ==0 :
            flag=False
            break
        stack.append(asc.pop(0))
        sol.append("+")
    elif arr[0] == stack[-1] :
        dest.append(stack.pop(-1))
        arr.pop(0)
        sol.append("-")
    else:
        flag=False
        break
 

if(flag):
    for i in sol:
        print(i)
else:
    print("NO")