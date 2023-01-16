def solution(m, n, puddles):
    answer = 0
    point=[[0]*(m+1) for i in range(0,n+1)]
    for i in range(0,len(puddles)):
        puddleX=puddles[i][0]
        puddleY=puddles[i][1]
        point[puddleY][puddleX]=-1
    print(point)
    point[1][0]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if point[i][j]==-1:
                continue
            if point[i-1][j]<0 and point[i][j-1]<0 :
                point[i][j]=0
            elif point[i][j-1]<0 :
                point[i][j]=point[i-1][j]
            elif point[i-1][j]<0 :
                point[i][j]=point[i][j-1]
            else:
                point[i][j]=point[i][j-1]+point[i-1][j]
    print(point)
    answer=point[n][m]
    return answer%1000000007

print(solution(4,3,[[1,2]]))