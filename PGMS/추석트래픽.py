"""
https://school.programmers.co.kr/learn/courses/30/lessons/17676
추석 트래픽 : 복잡한 입력 처리
"""


def solution(lines):
    cand = []
    pair = []
    for line in lines:
        _, time, duration = line.split(' ')
        h, m, s = map(float, time.split(':'))
        s += 3600*h + 60*m
        ms = int(s*1000)
        durms = int(float(duration[0:-1])*1000)
        cand.append(ms-durms+1)
        cand.append(ms)
        pair.append([ms-durms+1, ms])

    answer = 0
    print(pair)
    for candVal in cand:
        temp1 = 0
        temp2 = 0
        for p in pair:
            start, end = p
            if start -1000 <= candVal and candVal <= end:
                temp1+=1
            elif start <= candVal and candVal <= end + 1000:
                temp2 += 1
        answer = max(temp1,temp2,answer)

        
    return answer

print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))

# print(solution([
# "2016-09-15 20:59:57.421 0.351s",
# "2016-09-15 20:59:58.233 1.181s",
# "2016-09-15 20:59:58.299 0.8s",
# "2016-09-15 20:59:58.688 1.041s",
# "2016-09-15 20:59:59.591 1.412s",
# "2016-09-15 21:00:00.464 1.466s",
# "2016-09-15 21:00:00.741 1.581s",
# "2016-09-15 21:00:00.748 2.31s",
# "2016-09-15 21:00:00.966 0.381s",
# "2016-09-15 21:00:02.066 2.62s"
# ]))


# 2003 ~ 4002
# 5001 ~ 7000