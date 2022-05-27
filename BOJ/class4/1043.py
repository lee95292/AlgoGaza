"""
1043 거짓말
진실을 아는 사람 리스트 know_num에 추가, 
know_num 을 순회하면서 know_num이 포함된 파티의 인원을 know_num에 추가, 진실인 파티로 설정
"""
n,m = list(map(int,input().split()))

arr = list(map(int,input().split()))
know_num = arr[1:]

attendee = [[] for _ in range(m)]
isTruth = [False]*m
for i in range(m):
    attendees = list(map(int,input().split()))[1:]
    attendee[i] = attendees

while know_num:
    num = know_num.pop()

    for i in range(m):
        if num in  attendee[i] and isTruth[i] == False:
            know_num.extend(attendee[i])
            isTruth[i] = True
print(isTruth.count(False))