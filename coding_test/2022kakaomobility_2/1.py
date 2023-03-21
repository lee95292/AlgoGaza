"""
Solution: 
자동차는 단순 덧셈계산이지만 자전거와 대중교통은 이전정보를 저장해두어야합니다.
연속으로 도보를 한 경우에 최소시간과
연속 도보시간이 없는 경우의 최소시간을 각각 저장해 최솟값으로 갱신해줍니다.
"""

def solution(infos, m):
    cartime = 0
    bw,bnw = [0,0],0 # bikework, bike_notwalk
    pw,pnw = [0,0],0
    for info in infos:
        car, bike, pub, walk = info
        cartime += car

        bnw_tmp = min([bw[0] + bike, bnw+bike])
        if bnw+walk > bw[0]+walk and bw[1]+walk <= m: #  걷기
            bw = [bw[0]+walk, bw[1]+walk]
        elif walk <= m: # 자전거 > 걷기
            bw = [bnw+walk, walk]
        else:
            bw = [bnw+101, walk]
        bnw = bnw_tmp
        # print(bw,bnw)


        if pub == -1:
            pub = 101
        pnw_tmp = min([pw[0] + pub, pnw+pub])
        if pnw+walk > pw[0]+walk and pw[1]+walk <= m: #  걷기
            pw = [pw[0]+walk, pw[1]+walk]
        elif walk<=m : # 교통 > 걷기
            pw = [pnw+walk, walk]
        else:
            pw = [pnw+101,walk]
        pnw = pnw_tmp
        # print(pw,pnw)

    return min(cartime, pnw, bnw ,pw[0], bw[0])

# print(solution([[20, 40, -1, 60], [50, 20, 40, 30], [10, 30, 10, 20], [40, 10, 30, 50]], 60))

# print(solution([[100, 80, 10, 20], [100, 60, -1, 40]], 30))
print(solution([[100,20,100,10], [100,20,100,10], [100,20,100,10], [100,100,100,10]],30))

"""
car     bike    pub     walk
100     80      10      20 
100     60      -1      40
"""