#Nomor 1

class Counter:
    def __init__(self):
        self.value = 0
    
    def reset(self):
        self.value = 0
    
    def click(self):
        self.value += 1
    
    def getValue(self):
        return self.value
tally = Counter()
tally.reset()
tally.click()
result = tally.getValue()
print(result)  
tally.click()
result = tally.getValue()
print(result)  

#nomor 2
class CashRegister:
    def __init__(self):
        self.total = 0.0
        self.count = 0
    
    def additem(self, price):
        self.total += price
        self.count += 1
    
    def getTotal(self):
        return self.total
    
    def getCount(self):
        return self.count

register1 = CashRegister()
register1.additem(1.95)
register1.additem(0.95)
register1.additem(2.50)

register2 = CashRegister()
register2.additem(3.75)
register2.additem(0.15)
register2.additem(2.25)
register2.additem(1.80)

print("Register 1 sells", register1.getCount(), "items, with the total amount of $", register1.getTotal())
print("Register 2 sells", register2.getCount(), "items, with the total amount of $", register2.getTotal())

#Nomor 3
from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        common_divisor = gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def to_float(self):
        return self.numerator / self.denominator

fraction1 = Fraction(1, 3)
fraction2 = Fraction(2, 5)

print("Fraction 1:", fraction1)
print("Fraction 1 as float:", fraction1.to_float())

print("Fraction 2:", fraction2)
print("Fraction 2 as float:", fraction2.to_float())

