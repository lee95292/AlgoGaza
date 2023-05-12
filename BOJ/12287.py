n = int(input())
pathmap =[]
def changeMap(s):
    if s=='.' or s =='-':
        return 0
    return 1
for i in range(n):
    pathmap.append(list(map(changeMap, input().split())))


visit =[0]
def findPath()
