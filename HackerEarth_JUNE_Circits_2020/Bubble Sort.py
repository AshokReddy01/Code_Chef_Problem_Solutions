from sys import stdin
input = stdin.readline
from collections import Counter as count_values

def input_data():
    return list(map(int,input().split()))
def bs(data):
    count = 0
    n = len(data)
    ok = True
    while ok:
        ok = False
        count += 1
        for i in range(n-1):
            if data[i]> data[i+1]:
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
                ok = True
    return count



def source():
    a = int(input())
    data = input_data()
    return bs(data)



if __name__ == "__main__":
    
    
    value = source()
    print(value)