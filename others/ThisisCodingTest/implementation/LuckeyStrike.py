n = input()
ln = len(n)
sum=0
for i in range(ln//2):
    sum += int(n[i]) - int(n[ln-1-i])
    
if sum == 0 :
    print("LUCKY")
else:
    print("READY")