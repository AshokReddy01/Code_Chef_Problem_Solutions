'''
Chef and Icecream 

Problem Code: CHFICRM

'''
def process(data):
    ice_cream = 5
    chef_balance = {5:0,10:0,15:0}
    change = 0


    if data[0]  != ice_cream:
        return 'NO'

    for i in data:
        # print()
        
        # print()
        if i == 5:
            chef_balance[5] += 1
        else: 
            change = i - ice_cream
            
            if chef_balance[change] < 1:
                while change:
                    
                    if chef_balance[5] !=0 and change//5 <= chef_balance[5] :
                        chef_balance[5] -= 1
                        change -= 5
                        continue
                    
                    return 'NO'
                chef_balance[i] += 1
            else:
                chef_balance[change] -= 1
                chef_balance[i] += 1
    
    return 'YES'








def main():
    for test in range(int(input())) :

        size_of_customers = int(input())  
        data = list(map(int,input().split()))
        print(process(data))
        

if __name__ == "__main__":
    main()
    



    