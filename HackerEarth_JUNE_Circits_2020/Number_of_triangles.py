from sys import stdin
input = stdin.readline
from collections import Counter as count_values
from itertools import combinations as cr
def input_data():
    return list(map(int,input().split()))

def source():
    data = input_data()
    exc = data[1:]
    points = list(i for i in range(1,data[0]+1) if i not in exc)
    return len(list(cr(points,3)))


if __name__ == "__main__":
    
    for test in range(int(input())):
        print(source())