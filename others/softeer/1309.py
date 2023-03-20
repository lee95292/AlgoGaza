"""
3
40 80 70
50 10 20
100 70 30
"""
# N = int(input())
# grid = []
# for i in range(N):
#     grid.append([[x,i+1] for i,x in enumerate(map(int, input().split()))])
# grid.append([[0,i+1] for i in range(N)])
# print(grid)
# for i in range(N):
#     grid[3][i][0] = grid[2][i][0] + grid[1][i][0] + grid[0][i][0]
# answer = [[0]*N for _ in range(4)]
# for i in range(4):
#     grid[i].sort(key=lambda x: -x[0])
#     for j in range(N):
#         if grid[i][j-1][0] == grid[i][j][0]:
#             answer[i][grid[i][j][1]-1] = answer[i][j-1]+1
#         else:
#             answer[i][grid[i][j][1]-1] = j+1
# print(answer)

MAX_SCORE = 1002
MAX_TOTAL_SCORE = 3002
totalScoreCounts = [0]*(MAX_TOTAL_SCORE)

N = int(input())
totalScores = [0]*N
for i in range(3):
    scores = list(map(int,input().split()))
    scoreCounts = [0] * MAX_SCORE
    for k in range(N):
        totalScores[k] += scores[k]
        scoreCounts[scores[k]] += 1
    for k in range(MAX_SCORE-2,-1,-1):
        scoreCounts[k]+=scoreCounts[k+1]
    for score in scores:
        print(scoreCounts[score+1]+1,end=' ')
    print()
for i in range(N):
    totalScoreCounts[totalScores[i]] +=1

for i in range(MAX_TOTAL_SCORE-2,-1,-1):
    totalScoreCounts[i]+=totalScoreCounts[i+1]
for score in totalScores:
    print(totalScoreCounts[score+1]+1, end=' ')


