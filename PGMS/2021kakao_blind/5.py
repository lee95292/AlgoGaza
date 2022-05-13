def parseSec(time):
    sec = 0
    for idx,t in enumerate(time.split(':')):
        sec += 60**(2-idx) * int(t)
    return sec

def solution(play_time, adv_time, logs):
    play_time = parseSec(play_time)
    adv_time = parseSec(adv_time)
    startdict= {}
    enddict={}
    for idx,log in enumerate(logs):
        times = log.split('-')
        logs[idx] = [parseSec(times[0]), parseSec(times[1])]
        startdict[parseSec(times[0])] = parseSec(times[1])
        enddict[parseSec(times[1])] = parseSec(times[0])


    startlist = sorted(startdict)
    endlist=sorted(enddict)
    print(startlist)
    print(endlist)
    sidx= -1
    max_runtime,max_index  = 0,0
    while sidx < len(startlist)-1:
        eidx=len(endlist)-1
        sidx +=1
        adv_runtime = 0
        print(sidx,'sidxx=====' )
        sidx_ = sidx
        while  sidx_ < len(startlist) and  startlist[sidx_] <= startlist[sidx] +adv_time :
            adv_runtime +=  startlist[sidx] -startlist[sidx_] + adv_time
            print('start',sidx_, startlist[sidx] -startlist[sidx_] + adv_time)
            sidx_ +=1
        
        while eidx > 0 and endlist[eidx-1] > startlist[sidx]:
            eidx -= 1
        print(eidx)

        while eidx < len(endlist) and startlist[sidx] + adv_time > endlist[eidx] :
            adv_runtime += startlist[sidx] + adv_time - endlist[eidx]
            print('end',eidx,startlist[sidx] + adv_time - endlist[eidx])
            eidx +=1 
        if max_runtime < adv_runtime :
            max_runtime,max_index = adv_runtime,sidx
        
        if startlist[sidx]  + adv_time > play_time:
            break
    answer = ''
    print(max_runtime)
    print(max_index)
    return answer

print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))