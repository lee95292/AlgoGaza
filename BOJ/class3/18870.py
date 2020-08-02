n = input()
locations = list(map(int, input().split()))

sortedLocations = sorted(list(set(locations)))

dictLoc = {}


for idx in range(len(sortedLocations)):
    dictLoc[sortedLocations[idx]] = idx

for loc in locations:
    print(dictLoc[loc],end=' ')
