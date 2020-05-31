for test in range(int(input())):
    data = list(map(int,input().split()))
    string = input()
    d = {}
    for i in string:
        if i in d.keys():
            value = d[i]
            value += 1
            d[i] = value
        else:
            d[i] = 1

    for i in range(data[1]):
        count = 0
        for j in range(int(input())):
            for key in d:

                if d[key] == 0:
                    pass
                else:
                    value = d[key]
                    value -= 1
                    d[key] = value
        for key in d:
                if d[key] == 0:
                    pass
                else:
                    count += d[key]
        #print(d)
        print(count)

    