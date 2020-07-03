from sys import stdin
input = stdin.readline


def input_data():
    return list(map(int,input().split()))

def difference(x,y):
    if x != y:
        return y-x
    return 0



def source():
    a = input_data()
    b = input_data()
    if a==b:
        return 0
    count = 0
    l = set(map(difference, a,b))

    if 0 in l:
        l.remove(0)

    return len(l)




import timeit
if __name__ == "__main__":
    
    for test in range(int(input())):
        value = source()
        print(value)