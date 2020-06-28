'''
Chef and Demonetisation 
'''
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
    if S%2 != 0 or S == 1:
        count +=1
        S -= 1
    temp= (S//N)
    S -= temp*N
    count += temp
    
    while ok:
        if S%2 != 0 or S == 1:
            count +=1
            S -= 1
        elif S <= 0: 
            return count
        elif S<N:
            N -= 2
            S -= N
            count +=1
        else:
            S -= N
            count +=1
        

        
            
    return count

                




if __name__ == "__main__":
    
    for test in range(int(input())):
        print(source())