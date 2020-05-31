for i in range(int(input())):
    stack = []
    size = int(input())
    data = list(map(int,input().split()))
    data.sort()
    d = data[:len(data)-2]
    print(len(d),end= ' ')
    for k in d:
        print(k,end=' ')
    print()