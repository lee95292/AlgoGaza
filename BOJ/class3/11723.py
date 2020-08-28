from sys import stdin


def infast(): return stdin.readline().strip()


n = int(infast())
preparedAll = [1 for i in range(1, 22)]
preparedEmpty = [0 for i in range(1, 22)]
mask = [0 for i in range(1, 22)]

for i in range(n):
    inp = infast().split()
    command = inp[0]
    num = -1
    if(len(inp) > 1):
        num = int(inp[1])
    if(command == 'add'):
        mask[num] = 1
    elif(command == 'check'):
        print(mask[num])
    elif(command == 'remove'):
        mask[num] = 0
    elif(command == 'toggle'):
        mask[num] = mask[num] ^ 1
    elif(command == 'all'):
        mask = preparedAll
    elif(command == 'empty'):
        mask = preparedEmpty
