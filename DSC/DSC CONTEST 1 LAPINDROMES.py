strings =[]
l = int(input())
for i in range(l):
  strings.append(input())

for i in strings:
  mid = 0
  nex = 0
  if len(i)%2 == 0:
    mid = (len(i)//2)
    nex = mid
  else:
    mid = (len(i)//2)
    nex = mid+1
  str1 , str2 = i[:mid],i[nex:]
  count = 0
  for k in range(len(str1)):
    if str2[k] in str1:
      count += 1
    else:
      print('NO')
      break
  
  if count == len(str1):
    s1 = []
    s2 = []
    de= []
    de2 = []
    for m in range(len(str1)):
      s1.append(str1[m])
      s2.append(str2[m])
      s1 , s2 = list(set(s1)),list(set(s2))
      s1.sort()
      s2.sort()

    for j in s1:
      de.append(str1.count(j))
    for j in s2:
      de2.append(str2.count(j))
    ch = True

    if de == de2:
      print('YES')
    else:
      print('NO')
      
