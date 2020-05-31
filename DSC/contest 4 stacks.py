def check(value):
    index = 0

    for v in stack:
        if v == value:
            return index+1
        elif v > value:
            return index
        else:
            pass
        index += 1
    return 'no'



for i in range(int(input())):
    stack = []
    size = int(input())
    data = list(map(int,input().split()))
    for d in data:
        #print(stack)
        if len(stack) == 0:
            stack.append(d)
        else:
            ch = check(d)
            if ch == 'no':
                stack.append(d)
            else:
                stack[check(d)]=d
    print(len(stack),end=' ')
    for x in stack:
        print(x,end=' ')
    print()