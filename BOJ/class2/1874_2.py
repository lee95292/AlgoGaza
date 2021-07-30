import sys
sys.stdin = open("input.txt", "r")

debug = False
n = int(input())
arr =[]
for i in range(n):
    arr.append(int(input()))

pos = 0 # 이전 STACK 값  
flag = True
stack = []
sol = []
asc = [i for i in range(1, n+1)]
#print(asc)
dest= []
for cur in arr:
    #print(pos,cur)
    if cur > pos : # 스택에 쌓아야 하는 경우
        for i in range(pos ,cur):
            if len(asc) > 0 and asc[0] <= cur: 
                sol.append("+")
                stack.append(asc.pop(0))
            else: #다 쌓은 경우 
                break
        pos = cur
        dest.append(stack.pop())
        sol.append("-")
    else:
        sout = stack.pop()
        dest.append(sout)
        if sout != cur:
            flag= False
            print("NO")
            break
        sol.append("-")
        pos = cur
 #   print(stack)

if(flag and not debug):
    for i in sol:
        print(i)
#print(dest)