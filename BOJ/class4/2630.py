n, m = list(map(int, input().split()))
alphabets = {}
forget = set()
for i in range(97, 97+26):
    alphabets[chr(i)] = set()

for i in range(n):
    word = input()
    alphaList = set(word)

    for alpha in alphaList:
        alphabets[alpha].add(i)
    # print(alphabets)

k = set()
for j in range(m):
    query = list(input().split())
    # print('----\n alpahbets', alphabets[query[1]])
    if(query[0] == '1'):
        forget.add(query[1])
        k = k.union(alphabets[query[1]])
    elif(query[0] == '2'):
        forget.remove(query[1])
        k = set()
        for f in forget:
            k = k.union(alphabets[f])

    # print('k', k)
    print(n-len(k))
