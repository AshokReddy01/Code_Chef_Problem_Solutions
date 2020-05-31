for i in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    m = 1000000000
    ans = 0
    for i in s:
        if m>i:
            m = i
        print(m)
        ans +=m
    print(ans)