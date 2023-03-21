# 0년 1월 2일 3시 4분 5초
format = [12*30*24*60*60, 30*24*60*60, 24*60*60, 60*60, 60, 1]
def transToSec(date):
    sec = 0 
    for i in range(1,len(date)+1):
        sec += format[-i] * date[-i]
    return sec

def transToDate(sec):
    date = []
    for i in range(6):
        date.append(sec//format[i])
        sec -= (sec//format[i]) * format[i]
    return date

# 2일 후 0시 0분 0초보다 시점이 뒤면 점프된것
def isJumped(sec1, sec2):
    d1 = transToDate(sec1)
    d1[2]+=2
    d1[3], d1[4], d1[5] = 0,0,0
    if sec2 >= transToSec(d1):
        return True
    return False

def getSavingPeriod(st, ed):
    d1, d2 = transToDate(st), transToDate(ed)
    d1[3], d1[4], d1[5], d2[3], d2[4], d2[5] = 0,0,0,0,0,0
    return (transToSec(d2)- transToSec(d1)) // format[2] + 1
def solution(s, times):
    startDate, nowDate  = transToSec(list(map(int, s.split(':')))), transToSec(list(map(int, s.split(':'))))
    everydaySaving = 1

    for time in times:
        interval = transToSec(list(map(int,time.split(":"))))
        nowDate += interval
        if everydaySaving == 1 and interval > format[2] and isJumped(nowDate-interval, nowDate):
            everydaySaving=0
    answer = [everydaySaving, getSavingPeriod(startDate,nowDate)]
    return answer

print(solution("2021:04:12:16:08:35", ["01:06:30:00", "01:04:12:00"]))

a= "2021:04:12:16:08:35"
b= transToSec(list(map(int,a.split(":"))))
c= transToDate(b)
print(a,b,c)

