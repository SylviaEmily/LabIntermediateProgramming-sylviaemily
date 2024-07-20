# class Fraction:
#     def __init__(self, numerator=0, denominator=1):
#         if denominator == 0:
#             raise ZeroDivisionError("Denominator cannot be zero.")
        
#         if not isinstance(numerator, int) or not isinstance(denominator, int):
#             raise TypeError("The numerator and denominator must be integers.")
        
#         if numerator == 0:
#             self._numerator = 0
#             self._denominator = 1
#         else:
#             if (numerator < 0 and denominator >= 0) or (numerator >= 0 and denominator < 0):
#                 sign = -1
#             else:
#                 sign = 1
            
#             a = abs(numerator)
#             b = abs(denominator)
#             while a % b != 0:
#                 tempA = a
#                 tempB = b
#                 a = tempB
#                 b = tempA % tempB
            
#             self._numerator = sign * abs(numerator) // b
#             self._denominator = abs(denominator) // b
    
#     def __str__(self):
#         return f"{self._numerator}/{self._denominator}"
    
#     def __add__(self, other):
#         if isinstance(other, Fraction):
#             new_numerator = self._numerator * other._denominator + other._numerator * self._denominator
#             new_denominator = self._denominator * other._denominator
#             return Fraction(new_numerator, new_denominator)
#         else:
#             raise TypeError("Can only add two Fraction objects")
    
#     def __sub__(self, other):
#         if isinstance(other, Fraction):
#             new_numerator = self._numerator * other._denominator - other._numerator * self._denominator
#             new_denominator = self._denominator * other._denominator
#             return Fraction(new_numerator, new_denominator)
#         else:
#             raise TypeError("Can only subtract two Fraction objects")
    
#     def __mul__(self, other):
#         if isinstance(other, Fraction):
#             new_numerator = self._numerator * other._numerator
#             new_denominator = self._denominator * other._denominator
#             return Fraction(new_numerator, new_denominator)
#         else:
#             raise TypeError("Can only multiply two Fraction objects")
    
#     def __truediv__(self, other):
#         if isinstance(other, Fraction):
#             new_numerator = self._numerator * other._denominator
#             new_denominator = self._denominator * other._numerator
#             if new_denominator == 0:
#                 raise ZeroDivisionError("Division by zero in fraction result")
#             return Fraction(new_numerator, new_denominator)
#         else:
#             raise TypeError("Can only divide two Fraction objects")
    
#     def __eq__(self, other):
#         return self._numerator == other._numerator and self._denominator == other._denominator
    
#     def __ne__(self, other):
#         return not self.__eq__(other)
    
#     def __lt__(self, other):
#         return self._numerator * other._denominator < self._denominator * other._numerator
    
#     def __le__(self, other):
#         return self._numerator * other._denominator <= self._denominator * other._numerator
    
#     def __gt__(self, other):
#         return self._numerator * other._denominator > self._denominator * other._numerator
    
#     def __ge__(self, other):
#         return self._numerator * other._denominator >= self._denominator * other._numerator
    
    
def __init__(self, numerator = 0, denominator = 1) :
    if denominator == 0 :
        raise ZeroDivisionError("Denominator cannot be zero.")

    if (not isinstance(numerator, int) or not isinstance(denominator, int)) :
        raise TypeError ("The numerator and denominator must be integers.")

    if numerator == 0 :
        self._numerator = 0
        self._denominator = 1
    else :
        if (numerator < 0 and denominator >= 0 or numerator >= 0 and denominator < 0) :
           sign = -1
        else :
           sign = 1
        a = abs(numerator)
        b = abs(denominator)
        while a % b != 0 :
            tempA = a
            tempB = b
            a = tempB
            b = tempA % tempB
        self._numerator = abs(numerator)
        self._denominator = abs(denominator)  

def __repr__ (self) :
    return str 


