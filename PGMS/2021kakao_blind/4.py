def solution(n, s, a, b, fares):
    maxv = 100000000
    faredp = [[maxv for _ in range(n)] for _ in range(n)]

    for fare in fares:
        x,y,f= fare
        faredp[x-1][y-1] ,faredp[y-1][x-1]= f,f

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    faredp[i][j],faredp[j][i] = 0,0
                faredp[i][j] = min(faredp[i][j] , faredp[i][k] + faredp[k][j])
                faredp[j][i] = faredp[i][j]
    
    minv = maxv
    for i in range(n):
        minv = min(minv, faredp[s-1][i] + faredp[i][a-1] + faredp[i][b-1])
        # print(i,minv,faredp[s-1][i] , faredp[i][a-1] ,faredp[i][b-1])
    return minv


print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))