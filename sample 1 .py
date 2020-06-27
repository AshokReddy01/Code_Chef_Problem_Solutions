from sys import stdin
input = stdin.readline

def input_data():
    return list(map(int,input().split()))

def source():
    d = {'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    s = 0
    data = input_data()
    count = 0
    for i in range(data[0],data[1]+1):
        if i == 1:
            continue
        count +=1
    print(count)
    value = hex(count)
    value = value[2:]
    print(value)
    for i in value:
        if i in ['a','b','c','d','e','f']:
            s += d[i]
        else:
            s += int(i)

    return s



if __name__ == "__main__":
    
    for test in range(int(input())):
        value = source()
        print(value)