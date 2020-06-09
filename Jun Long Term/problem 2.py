def process(l,pair):
    if len(l) <= 1 :
        print(pair)
        return 0
    else:
        a = l[0]
        l = l[1:]
        if a == 'x' and l[0] == 'y':
            pair += 1
            process(l[1:],pair)
            return 
        elif a == 'y' and l[0] == 'x':
            pair += 1
            process(l[1:],pair)
            return
        else:
            process(l,pair)
            return



if __name__ == '__main__':
    for test in range(int(input())):
        string = input()

        process(string,pair=0)