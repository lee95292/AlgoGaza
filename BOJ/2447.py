
n = int(input())
arr = [[1]*n for i in range(n)]

def ast(n, x, y): 
    if n == 1 : 
        return
    for i in range(3):
        for j in range(3):
            if i == 1 and j==1:
                #print(n,x,y)
                for q in range(y+n//3, y+2*n//3):
                    for w in range(x+n//3, x+2*n//3):
                        #print('qw',q,w)
                        arr[q][w] =0
            else:
                ast(n//3, x+i*n//3, y+j*n//3)


ast(n,0,0)
for i in range(n):
    #print(i)
    for j in range(n):
        if arr[i][j] == 1:
            print('*',end='')
        else:
            print(' ',end='')
    print('')
