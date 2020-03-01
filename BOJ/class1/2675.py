n = int(input())

for i in range(n):
    k, word = input().split()
    k = int(k)
    for j in word:
        print(j*k, end='')
    print()
