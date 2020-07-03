def divider(d=[]):
    li = []
    j=0
    sam = []
    for i in d:

        if i-j <= 2:

            sam.append(i)
            j = i
        else:
            li.append(sam)
            sam=[]
            sam.append(i)
            j=i
    li.append(sam)
    return li




if __name__ == "__main__":
    for test_case in range(int(input())):
        sets = []
        members = int(input())
        data = list(map(int,input().split()))
        data = divider(data)
        print(f"{len(min(data))} {len(max(data))}")