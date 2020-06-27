from sys import stdin
input = stdin.readline
from collections import Counter as count_values

def input_data():
    return list(map(int,input().split()))

def reduce_a(temp,a):
    return list(map(lambda x:x-1,a))
def slice(a):
    for i in range(len(a)):
        if a[i] == 0:
            return a[:i]
            
def source():
    s = int(input())
    a = input_data()
    count = 0
    ok = True
    while ok:
        temp = 0
        print(a)
        print("Count ",count)
        if 0 in a :
            a = slice(a)
        

        s = len(a)
        temp = min(a)
        
        

        a = reduce_a(temp,a)
        count += temp*s
        
        
        

    
            


if __name__ == "__main__":
    
    for test in range(int(input())):
        value = source()
        print(value)