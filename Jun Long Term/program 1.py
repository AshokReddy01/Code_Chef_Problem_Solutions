def reduce(i):
    if i > price:
        return price
    return i

price = 0
if __name__ == "__main__":
    for test_sample in range(int(input())):
        condictions = list(map(int , input().split()))
        price = condictions[1]
        data = list(map(int , input().split()))
        sample = list(map(reduce , data))
        print(sum(data) - sum(sample))