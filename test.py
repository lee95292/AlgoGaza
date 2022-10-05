def list2int(lst, result):
  if len(lst) == 0 :
    return result
  k = lst.pop()
  if result == '':
    s = k
  else:
    r = len(str(result))
    s= 10**r*k + int(result)

  return list2int(lst, s)

print(list2int([1,110,1],''))