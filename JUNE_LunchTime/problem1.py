from sys import stdin
input = stdin.readline
from collections import Counter as count_values
import math
def input_data():
    return map(int,input().split())

def source():
    S , N = input_data()
    count = 0
    ok = True
    while ok:
        print(S)
        if  S == 0:
            return count
        elif S==1:
            return count+1
        else:
            if S >= N:
                count = S//N
                S -= count * N
            elif S%2 != 0:
                count += 1
                S -=1
            else:
                S=0
                count +=1
            
    return count

                




if __name__ == "__main__":
    
    for test in range(int(input())):
        print(source())