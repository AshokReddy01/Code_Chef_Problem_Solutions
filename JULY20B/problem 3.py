import os
import sys
from io import BytesIO, IOBase


from collections import Counter as count_values
import math

def input_data():
    return list(map(int,input().split()))

def source():
    city , vaccin_count = map(int,input().split())
    city_population = input_data()
    temp = vaccin_count
    city_population.sort()
    count = 0
    print()
    member = city_population[-city]
    while city > 0:
        
        
        print(member,vaccin_count)
        if member == 0:
            city -= 1
            member = city_population[-city]
        
        elif member > vaccin_count:
            vaccin_count *=  2
            count +=1
        elif member<=vaccin_count:
            
            vaccin_count = temp+ (member * 2)
            member = 0

            count += 1
    return count


def main():
    for _ in range(int(input())):
        print(source())



# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")





if __name__ == "__main__":
    main()

