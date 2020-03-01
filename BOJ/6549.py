histos = []
while(True):
    tmp = input()
    if(tmp == '0'):
        break

    histos.append(list(map(int, tmp.split())))

for histo in histos:

    lenHisto = histo[0]
    histo = histo[1:]

    sortedHisto = list(set(histo.copy()))
    sortedHisto.sort()

    maxArea = len(sortedHisto)
    histoSize = []
    visit = [1 for x in histo]

    for i in sortedHisto:

        lenWitdth = 0
        tmpWidth = 0
        for idx, j in enumerate(histo):
            if(visit[idx] and i <= j):
                tmpWidth = tmpWidth+1
            else:
                visit[id0x] = 0
                lenWitdth = max(tmpWidth, lenWitdth)
                tmpWidth = 0

        if(lenWitdth == 0):
            lenWitdth = tmpWidth
        histoSize.append(lenWitdth*i)

    print(max(histoSize))
