T = int(input())
for _ in range(T):
  N, x, y = map(int, input().split())
  result = []
  for i, digit in enumerate(reversed(str(N))):
    if digit == str(x):
      result.append(y)
    elif digit == str(y):
      result.append(x)
    else:
      result.append(digit)
  result.reverse()
  print(''.join(result))
