def fac(num):
    if num == 0 or num ==1:
        return 1
    else:
        return num*fac(num-1)

def digits_count(value):
    c = 0
    while value>0:
        c += 1
        value //=10
    return c
    
num = int(input())
value = fac(num)
value = value**num
count = digits_count(value)
print(count)