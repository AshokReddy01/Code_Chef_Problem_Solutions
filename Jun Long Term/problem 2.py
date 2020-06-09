'''
Chef and String 

Problem Code: XYSTR

'''


def process(data):
    pairs_found = 0
    free_pass = False
    first_persion = None
    for i in data:
        if free_pass:
            first_persion = i
            free_pass = False
            continue
        if first_persion == None:
            first_persion = i
            continue
        if (first_persion == 'x' and i == 'y') or (first_persion == 'y' and i == 'x'):
            free_pass = True
            pairs_found +=1
    return pairs_found

            





if __name__ == '__main__':
    for test in range(int(input())):
        string = input()

        print(process(string))