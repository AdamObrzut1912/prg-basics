class C:
    def __init__(self,sectors):
        self.sectors = sectors
    
    def m1(self, s, n):
            self.sectors[s] = n

    def m2(self,s):
        sum = 0
        for i in s:
            if i in self.sectors:
                sum += self.sectors[i]
        return sum
