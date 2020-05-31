for test in range(int(input())):
    stack = []
    h = 0
    count = 0
    data = input()
    for i in data:
        if i == '>' and count == 0:
            break
        else:
            count = 1
            if i == '<':
                stack.append(i)
                if h < len(stack):
                    h = len(stack)
            elif len(stack)>0 and stack[-1] == '<' and i == '>' :
                stack.pop()
            else:
                stack.append(i)
            if h < len(stack):
                    h = len(stack)
        print(stack)
    if count == 1 and len(stack)==0:
        print(len(data))
    else:
        print(h)
                
