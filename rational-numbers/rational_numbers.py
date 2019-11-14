from __future__ import division
from math import gcd


class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self.reduce()

    def reduce(self):
        if self.denom == 0:
            raise ZeroDivisionError
        val = gcd(self.numer, self.denom)
        self.numer //= val
        self.denom //= val
        if self.denom < 1:
            self.numer *= -1
            self.denom *= -1

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        self.numer = (self.numer * other.denom) + (self.denom * other.numer)
        self.denom *= other.denom
        self.reduce()
        return self

    def __sub__(self, other):
        self.numer = (self.numer * other.denom) - (self.denom * other.numer)
        self.denom *= other.denom
        self.reduce()
        return self

    def __mul__(self, other):
        self.numer *= other.numer
        self.denom *= other.denom
        self.reduce()
        return self

    def __truediv__(self, other):
        self.numer *= other.denom
        self.denom *= other.numer
        self.reduce()
        return self

    def __abs__(self):
        if self.numer < 1:
            self.numer *= -1
        return self

    def __pow__(self, power):
        self.numer **= power
        self.denom **= power
        return self

    def __rpow__(self, base):
        return (base**self.numer)**(1/self.denom)
