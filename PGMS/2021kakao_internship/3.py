import sys
sys.setrecursionlimit(10**6)
n,k=8,2
cmd=["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
#cmd=["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
#cmd=["D 3","C","C","C"]

arr = [0 for x in range(n)]

delSegtree= [0] * (n*2)

def init(left,right,node):
    if left == right:
        delSegtree[node] = arr[left] 
        return delSegtree[node]

    mid = (left + right) //2
    delSegtree[node] =init(left, mid,node*2) + init(mid+1,right,node*2+1)
    return delSegtree[node]

# start,end : 재귀함수에서 합을 담당하는 구간
# left, right: 합을 구해야하는 구간
def sectionsum(left,right,node=1,start=0, end=n-1):
    #완전 미포함
    if left > end or right < start:
        return 0
    #완전포함
    if start >= left and end <=right:
        return delSegtree[node]
    
    # 부분포함
    mid = (start+end)//2
    return sectionsum(left,right,node*2,start, mid) + sectionsum(left,right,node*2+1,mid+1,end)

def update(index,diff,node=1,left=0,right=n-1):
    if left > index or right <index :
        return 0

    delSegtree[node] +=diff
    mid = (left+right)//2
    if left != right:
        update(index,diff,node*2,left,mid)
        update(index,diff,node*2+1,mid+1, right)

def getRealPoint(a,b):
    diff = sectionsum(min(a,b),max(a,b))
    if diff > 0:
        if max(a,b)+diff >= n:
            return -1
        if a == b:
            n = getRealPoint(a+1,b+diff)
            if n == -1:
                return -1
            return diff+n
    return b

def getRealPoint(a,b):
    diff=0
    while True:
        diff = sectionsum(min(a,b),max(a,b))
        if diff == 0:
            break
        if a == b:
            if a + diff >= n:
                return getRealPoint(a,b-1)+1
            else:
                a=b+1
                b = b + diff
        elif b>a:
            a=b+1
            b = b + diff
        else:
            a=b-1
            b=b-diff
    return b
init(0,n-1,1)


deleted= [0 for i in range(n)]
delstack = []

for command in cmd:
    c,v = command,0
    if len(command) > 1:
        c,v = command.split()
        v = int(v)
    if c == 'U':
        k = getRealPoint(k,k-v)            
    if c == 'D':
        k = getRealPoint(k,k+v)
    if c == 'C':
        deleted[k] = 1
        update(k,1)
        delstack.append(k)
        k = getRealPoint(k,k)        
    if c == 'Z':
        z = delstack.pop()
        deleted[z]=0
        update(z,-1)
        k = getRealPoint(k,k)
    print()
    print(deleted)
    print(command, k)

answer = ''
for i in deleted:
    if i == 0:
        answer += 'O'
    elif i == 1:
        answer += 'X'

print(answer)