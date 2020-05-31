def main():
    total = 24*5
    for test in range(int(input())):
        data = list(map(int,input().split()))
        hours = data[-1]
        data = data[:-1]
        data = list(map(lambda x:x*hours,data))
        if sum(data)<=total:
            print("No")
        else :
            print("Yes")
        #print(data)
        
if __name__ == "__main__":
    main()