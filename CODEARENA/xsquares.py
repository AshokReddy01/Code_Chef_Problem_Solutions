from sys import stdin
input = stdin.readline
from collections import Counter as count_values
def input_data():
    return list(map(int,input().split()))
def source():
    stack = 0
    temp = 0
    ok = True
    n , h = map(int,input().split())
    data = input_data()
    for i in range(n+1):
        if data[i] == h:
            ok = True
            if ok:
                temp +=1
            
        else:
            ok = False
            if stack <= temp:
                stack = temp
            temp = 0
    return stack
        
            


    


if __name__ == "__main__":
    
    for test in range(int(input())):
        value = source()
        print(value)