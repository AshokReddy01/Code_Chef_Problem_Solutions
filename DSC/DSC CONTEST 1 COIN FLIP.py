for test in range(int(input())):
  for games in range(int(input())):
    data = list(map(int,input().split()))
    I = data[0]
    N = data[1]
    G = data[2]
    coins = []
    for i in range(1,N+1):
      if I == 1:
        coins.append('H')
      else:
        coins.append('T')
      for j in range(i):
        if coins[j] == 'H':
          coins[j] = 'T'
        else :
          coins[j] = 'H'
      print(coins)
    #print(coins)
    
    if G == 1 :
      print(coins.count('H'))
    else:
      print(coins.count('T'))