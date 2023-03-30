N,K = map(int,input().split())

namelenGrade = [[] for _ in range(21)]
names = []
for i in range(N):
    name = input()
    namelenGrade[len(name)].append(i)
answer = 0
for i in range(1,21):
