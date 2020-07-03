from sys import stdin
input = stdin.readline
import numpy as np
import random


def input_data():
    return list(map(int,input().split()))

def source():
    n = int(input())
    array = []
    ok = True
    num = 1
    for i in range(0,n):
        temp = []
        for i in range(0,n):
            temp.append(num)
            num+=1
        array.append(temp)
            
    array=np.array(array)
    
    return array


if __name__ == "__main__":
    
    for test in range(int(input())):
        value = source()
        print(value)