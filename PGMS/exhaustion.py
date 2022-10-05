# 프로그래머스 피로도 계산
# 완전탐색
from itertools import permutations
def solution(k, dungeons):
    
    answer = -1
    for order in permutations(dungeons, len(dungeons)):
        remain = k
        done=0
        for turn in order:
            minx, use = turn
            if minx <= remain:
                remain-=use
                done+=1
            else:
                break
        answer = max(answer, done)
    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))