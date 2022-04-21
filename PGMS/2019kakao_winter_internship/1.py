from ast import Continue


board = [
[1,0,0,0,0],
[1,0,1,0,3],
[1,2,5,0,1],
[1,2,4,4,2],
[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
moves=[1,1,1,1]
n= len(board)

lines = [[] for _ in range(n)]
for i in range(n):
    lines[i] = [board[j][i] for j in range(n) if board[j][i] >0]

answer = 0
stack = []
for move in moves:
    if len(lines[move-1]) == 0:
        continue
    stack.append(lines[move-1].pop(0))

    stackSize = len(stack)
    if stackSize >= 2 and stack[stackSize-2] == stack[stackSize-1]:
        stack.pop()
        stack.pop()
        answer += 2
print(answer)