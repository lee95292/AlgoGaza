# Bottum up 방식으로 삼각형 더하면서 올라가는 방식
def solution(triangle):
    answer = 0
    size = len(triangle)
    for i in range(size-2, -1, -1):  # 높이
        for j in range(0, len(triangle[i])):  # 밑변
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

    answer = triangle[0][0]
    return answer
