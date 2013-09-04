'''
Created on 3 Sep 2013

@author: brian
'''

class Rational(object):

    def __init__(self, numerator, denominator):
        """
        Initialise a rational number with the specified numerator and denominator
        """
        if denominator == 0:
            raise ValueError("Denominator must be non-zero")
        gcd = self.__gcd(numerator, denominator)
        self.numerator = numerator / gcd
        self.denominator = denominator / gcd
        self.__fixsign()
    
    def neg(self):
        """
        Return the negated version of this rational
        """
        return Rational(-self.numerator, self.denominator)
    
    def __neg__(self):
        return self.neg()
    
    def reciprocal(self):
        """
        Return the reciprocal version of this rational
        """
        return Rational(self.denominator, self.numerator)
    
    def add(self, other):
        """
        Return the sum of this rational and the specified other
        """
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                    self.denominator * other.denominator)
        
    def __add__(self, other):
        return self.add(other)
    
    def subtract(self, other):
        """
        Return the subtraction of the specified other from this rational
        """
        return self.add(other.neg())
    
    def __sub__(self, other):
        return self.subtract(other)
    
    def multiply(self, other):
        """
        Return the product of this rational and the specified other
        """
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)
    
    def __mul__(self, other):
        return self.multiply(other)
    
    def divide(self, other):
        """
        Return the division of this rational by the specified other
        """
        return self.multiply(other.reciprocal())
    
    def __div__(self, other):
        return self.divide(other)
    
    def isEqualTo(self, other):
        """
        Return true if the rationals are equal in value, false otherwise
        """
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __eq__(self, other):
        return self.isEqualTo(other)
    
    
    # Class private methods below
    def __str__(self):
        """
        Return the string representation of this rational
        """
        return str(self.numerator) + '/' + str(self.denominator)
    
    def __gcd(self, a, b):
        """
        Private method to calculate the greatest common divisor of two integers using
        Euclid's method
        """
        while (b != 0):
            tmp = a
            a = b
            b = tmp % b
        return -a if a < 0 else a
    
    def __fixsign(self):
        """
        Make sure a negative sign is associated with the numerator
        """
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

#
# Example usage
#
if __name__ == "__main__":
    x = Rational(1, 3)
    y = Rational(5, 7)
    z = -Rational(3, 2)
    
    # Show off the overridden infix operators
    print x - y - z
    print y + y
    print x * z
    print x / y + z
