def process(data):
    chef_balance = 0
    change = 0
    for i in data:
        if chef_balance == 0 :
            chef_balance = i
        else:
            change = i - 5
            if chef_balance >= change:
                chef_balance = i
                continue 
            return 'NO'
    return 'YES'
        
def check(i):
    if i % 5 ==0:
        return True
    return False


def main():
    for test in range(int(input())):
        
        size = int(input())
        data = list(map(int,input().split()))
        if size == 1:
            print("YES")
            continue
        d= list(filter(check,data))

        if len(data) == len(d):
            print(process(data))
        else:
            print('NO')
            

if __name__ == "__main__":
    chef_balance = 0
    main()
    



    