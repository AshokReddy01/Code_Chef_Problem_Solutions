for test_case in range(int(input())):
    sets = []
    members = int(input())
    data = list(map(int,input().split()))
    staring = 0
    nu = 0
    temp =[]
    for m in data:
        if staring == 0:
            nu = m
            temp.append(m)
            staring = 1
        else:
            if (m-nu) <= 2:
                temp.append(m)
                nu = m
            else:
                sets.append(temp)
                temp = []
                temp.append(m)
                nu = m
                staring = 0
        
    sets.append(temp)
    m = 0
    n = 2000
    for g in sets:
        l = len(g)
        if m < l:
            m = l
        if n >l:
            n = l
    print(n, end=" ")
    print(m)