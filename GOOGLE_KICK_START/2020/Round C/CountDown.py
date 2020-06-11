
from sys import stdin
input = stdin.readline
from collections import Counter as count_values

def source():
    n , k = map(int,input().split())
    data = list(map(int,input().split()))
    count = 0
    c=0
    ok = True
    if k not in data:
        return 0
    for i in range(k-1,n):
        ok = True
        for j in range(1,k+1):
            if ok:
                if data[i+1-j] != j :
                    ok =False
                continue
            break
        if ok:
            count += 1
    return count
            

if __name__ == "__main__":
    
    for test in range(int(input())):
        value = source()
        print(value)