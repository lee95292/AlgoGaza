from re import L


def solution(board, r, c):
    cards={}
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                cards[board[i][j]] = [j,i]
    
    for key in cards:
        x,y = cards[key]
        

    answer = 0
    return answer