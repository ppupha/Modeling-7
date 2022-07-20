from scipy.stats import chi2

class LinearCong:
    def __init__(self):
        self.current = 7
        self.m = 2.**31
        self.a = 12345
        self.c = 101234323

    def next(self, low=0, high=100):
        self.current = (self.a * self.current + self.c) % self.m
        result = int(low + self.current % (high - low))
        return result

class FileTable:
    def __init__(self):
        self.nums = None
        with open('nums.txt', 'r') as f:
            a = list(f.read().split('\n'))
            nums = [list(i.split()) for i in a]
                        
            self.nums = nums
            self.columns = len(self.nums[0])
            self.rows = len(self.nums)

            self.cur_x = 0
            self.cur_y = 0

    def next(self):
        self.cur_x += 1
        if self.cur_x == self.columns:
            self.cur_x = 0
            self.cur_y += 1
        if self.cur_y == self.rows:
            self.cur_y = 0

        return self.nums[self.cur_y][self.cur_x]

def ChiSquare(arr, a = None, b = None):
    if (a == None):
        a = min(arr)
    if (b == None):
        b = max(arr)
    tmp = [0 for i in range(b - a+1)]
    for i in arr:
        tmp[i - a] += 1

    n = len(arr)
    k = len(tmp)

    p = 1.0 / k

    chi = 0

    for i in tmp:
        chi += i * i
    chi = chi / p / n - n

    return (chi2.cdf(chi, k)) * 100, chi,


def output(RandomAlg, RandomTab, ChiAlg, ChiTab, isPrint = False):

    l = len(RandomAlg[0])

    n = min(l, 15)

    if (isPrint):

        print("|{:^10s}|{:^32s}|{:^32s}|".format("", "Алгоритмический метод", "Табличный метод"))
        print("|{:^10}|{:^10s}|{:^10s}|{:^10s}|{:^10s}|{:^10s}|{:^10s}|".format("", "1 разряд", "2 разряд", "3 разряд", "1 разряд", "2 разряд", "3 разряд"))

        for i in range(n):
            print("|{:^10}|{:^10d}|{:^10d}|{:^10d}|{:^10d}|{:^10d}|{:^10d}|".format(i,RandomAlg[0][i], RandomAlg[1][i], RandomAlg[2][i], RandomTab[0][i], RandomTab[1][i], RandomTab[2][i]))
        if (l > 10):
            print("|{:^10}|{:^10s}|{:^10s}|{:^10s}|{:^10s}|{:^10s}|{:^10s}|".format("...", "...", "...", "...", "...", "...", "..."))
    printformat = "|{:^10s}|{:^9.3f}%|{:^9.3f}%|{:^9.3f}%|{:^9.3f}%|{:^9.3f}%|{:^9.3f}%|"
    print(printformat.format("Chíquare",ChiAlg[0][0], ChiAlg[1][0], ChiAlg[2][0], ChiTab[0][0], ChiTab[1][0], ChiTab[2][0]))
    print("|{:^10s}|{:^10.3f}|{:^10.3f}|{:^10.3f}|{:^10.3f}|{:^10.3f}|{:^10.3f}|".format("Chíquare",ChiAlg[0][1], ChiAlg[1][1], ChiAlg[2][1], ChiTab[0][1], ChiTab[1][1], ChiTab[2][1]))

def main():
    algGen = LinearCong()
    tabGen = FileTable()
    n = 10000

    a, b = 0, 10
    _1DigitAlg = [algGen.next(a, b) for i in range(n)]
    a, b = 10, 100
    _2DigitAlg = [algGen.next(a, b) for i in range(n)]
    a, b = 100, 1000
    _3DigitAlg = [algGen.next(a, b) for i in range(n)]

    RandomAlg = [_1DigitAlg, _2DigitAlg, _3DigitAlg]

    _1DigTab = [int(tabGen.next()) % 10 for i in range(n)]
    j = 2
    _2DigTab = [int(tabGen.next()) % 90 + 10 for i in range(n)]
    j = 3
    _3DigTab = [int(tabGen.next()) % 900 + 100 for i in range(n)]
    RandomTab = [_1DigTab, _2DigTab, _3DigTab]
    

    ChiAlg = [ChiSquare(RandomAlg[0], 0, 9),  ChiSquare(RandomAlg[1], 10, 99), ChiSquare(RandomAlg[2], 100, 999)]
    ChiTab = [ChiSquare(RandomTab[0], 0, 9),  ChiSquare(RandomTab[1], 10, 99), ChiSquare(RandomTab[2], 100, 999)]

    output(RandomAlg, RandomTab, ChiAlg, ChiTab, 1)

main()



    
    
    
