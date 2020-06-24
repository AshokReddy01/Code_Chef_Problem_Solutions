from sys import stdin
input = stdin.readline
from collections import Counter as count_values
import math
def input_data():
    return list(map(int,input().split()))

def source():
    count = 0
    data = []
    N , B , M = map(int,input().split())
    chef_data = input_data()
    ok = True
    value = 0
    while ok:
        temp = []

        for _ in range(B):
            if value == N:
                ok = False
                break
            temp.append(value)
            value += 1
        data.append(temp)

    cache = []
    for i in chef_data:
        if i == 0 or i not in cache:
            count += 1
            cache = data[(math.floor(i/B))]
    


    return count




if __name__ == "__main__":
    
    for test in range(int(input())):
        print(source())