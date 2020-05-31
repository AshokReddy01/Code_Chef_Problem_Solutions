from itertools import combinations 

def fa(arr = [], *args):
  ma = max(arr)
  for l in range(1,ma):
    if l in arr:
      pass
    else:
      return l
  return ma+1
 
for i in range(int(input())):
  size = int(input())
  array = list(map(int,input().split()))
  from itertools import combinations 
  d = []
  for f in range(1,size+1):
    comb = combinations(array, f)
    for j in list(comb):
      d.append(list(j)) 
  #print('combination',d)
  total = 1
  #print(d)

  for com in d:
    total += fa(com)    
  
  print(total%998244353)
    
 
  
