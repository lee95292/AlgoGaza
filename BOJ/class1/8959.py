n = int(input())

arr = []
for i in range(n):
    score = 0
    ac = 1
    for j in input():
        if(j == 'O'):
            score = score+ac
            ac = ac+1
        else:
            ac = 1
    print(score)
