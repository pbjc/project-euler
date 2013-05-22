#===============================================================================
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# 
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# 
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# 
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
#===============================================================================

from Common import prod, gcd

class Fraction:
    
    def __init__(self, num, den):
        self.num = num
        self.den = den
    
    def __eq__(self, other):
        return self.num * other.den == other.num * self.den

specials = []
for d in range(11, 100):
    for n in range(11, d):
        if n == d or (n % 10 == 0 and d % 10 == 0):
            continue
        for c in str(n):
            if c in str(d):
                frac = Fraction(n, d)
                canc = Fraction(int(str(n).replace(c, '', 1)), int(str(d).replace(c, '', 1)))
                if frac == canc:
                    specials.append(frac)
num = prod([f.num for f in specials])
den = prod([f.den for f in specials])
print(den // gcd(num, den))