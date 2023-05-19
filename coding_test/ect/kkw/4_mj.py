import sys
input = sys.stdin.readline

def make_ans(n_x, n_y, distance):
   if ans[n_x][n_y] == -1:
      ans[n_x][n_y] = distance
   else:
      ans[n_x][n_y] = min(distance, ans[n_x][n_y])

n = int(input())
building = []
region = []
for i in range(n):
   line = input()
   region.append(line)
   for j in range(len(line)):
      if line[j] == '1':
         building.append([i, j])

ans = [[-1 for _ in range(n)] for _ in range(n)]
for b in building:
   x = b[0]
   y = b[1]
   ans[x][y] = 0
   for new_x in range(x-1, -1, -1):
      if region[new_x][y] == "1":
         break
      make_ans(new_x, y, abs(x-new_x))
      
   for new_x in range(x+1, n):
      if region[new_x][y] == "1":
         break
      make_ans(new_x, y, abs(x-new_x))

   for new_y in range(y-1, -1, -1):
      if region[x][new_y] == "1":
         break
      make_ans(x, new_y, abs(y-new_y))

   for new_y in range(y+1, n):
      if region[x][new_y] == "1":
         break
      make_ans(x, new_y, abs(y-new_y))
   
for a in ans:
   print(*a)