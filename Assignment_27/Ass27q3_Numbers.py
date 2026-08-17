class Numbers :

    def __init__ (self,Value):
        self.Value = int(Value) 

    def Prime(self):
        if self.Value <= 1:
            return False

        for i in range(2,int(self.Value**0.5)+1):
            if self.Value % i == 0:
                return False
            return True

    def Perfect(self):
        if self.Value <= 1:
            return False
        sum=1
        for i in range(2,int(self.Value**0.5)+1):
            if self.Value % i == 0:
                sum += i
                if i != self.Value//i:
                    sum += self.Value//i
        return sum==self.Value

    def Factors(self):
        fact_l=[]
        for i in range (1,self.Value+1):
            if self.Value % i == 0:
                fact_l.append(i)
        print(f"Factors of : {self.Value} : {fact_l}")

    def sumFactors(self):
        total=0
        for i in range(1,self.Value+1):
            if self.Value % i == 0:
                total += i
        return total

obj1=Numbers(6)
print(f"Is Prime ? {obj1.Prime}")
print(f"Is Perfect ? {obj1.Perfect}")
obj1.Factors()
print(f"Sum of Factors : {obj1.sumFactors}")            