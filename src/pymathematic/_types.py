from typing import Any, Callable, Self
from dataclasses import dataclass
from decimal import Decimal

from .errors import *
from .functions import *

@dataclass
class Number:
    value: int | Decimal

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.value})'
    
    def __str__(self) -> str:
        return f'{self.value}'
    
    def __int__(self) -> int:
        return int(self.value)
    
    def __float__(self) -> float:
        return float(self.value)

    def __add__(self, other: Self) -> Self:
        if not isinstance(other, Real):
            other = Real(other)
        
        return Real(self.value + other.value)

    def __sub__(self, other: Self) -> Self:
        if not isinstance(other, Real):
            other = Real(other)
        
        return Real(self.value - other.value)

    def __mul__(self, other: Self) -> Self:
        if not isinstance(other, Real):
            other = Real(other)
        
        return Real(self.value * other.value)

    def __truediv__(self, other: Self) -> Self:
        if not isinstance(other, Real):
            other = Real(other)
        
        return Real(self.value / other.value)

    def __floordiv__(self, other: Self) -> Self:
        if not isinstance(other, Real):
            other = Real(other)
        
        return Real(self.value // other.value)

    def __mod__(self, other: Self) -> Self:
        if not isinstance(other, Real):
            other = Real(other)
        
        return Real(self.value % other.value)

    def __pow__(self, other: Self) -> Self:
        if not isinstance(other, Real):
            other = Real(other)
        
        return Real(self.value ** other.value)

class NaturalInteger(Number):
    value: int

    def __init__(self, value: int) -> None:
        value = float(value)

        if value < 0 or int(value) != value:
            raise PositiveIntegerError

        self.value = int(value)

class Integer(Number):
    value: int

    def __init__(self, value: int):
        if int(float(value)) != float(value):
            raise IntegerError

        self.value = int(value)

class Rational(Number):
    def __init__(self, numerator: int, denominator: int | None = None) -> None:
        if isinstance(numerator, str) and denominator is None:
            parts = numerator.split('/')
            
            if len(parts) == 2:
                numerator, denominator = parts
            elif len(parts) == 1:
                numerator = parts[0]
            else:
                raise InvalidLiteralError((self.__class__, numerator))
            
        if denominator is None:
            denominator = 1
        
        numerator = Decimal(str(numerator))
        denominator = Decimal(str(denominator))

        if int(numerator) == numerator:
            numerator = int(numerator)
             
        if int(denominator) == denominator:
            denominator = int(denominator)

        if denominator == 0:
            raise DivisionByZeroError
        
        if denominator < 0:
            numerator *= -1
            denominator *= -1
        
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.numerator}/{self.denominator})"
    
    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"
    
    def __float__(self) -> float:
        return float(Decimal(self.numerator) / Decimal(self.denominator))

    def __int__(self) -> int:
        return int(float(self))

    def _simplify(self) -> None:
        _gcd = Decimal(str(gcd(self.numerator, self.denominator)))
        self.numerator = Decimal(str(self.numerator)) // _gcd
        self.denominator = Decimal(str(self.denominator)) // _gcd
    
    def __add__(self, other: Self) -> Self:
        if not isinstance(other, self.__class__):
            other = self.__class__(other)
        
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator

        return self.__class__(new_numerator, new_denominator)
    
    def __sub__(self, other: Self) -> Self:
        if not isinstance(other, self.__class__):
            other = self.__class__(other)
        
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator

        return self.__class__(new_numerator, new_denominator)

    def __mul__(self, other: Self) -> Self:
        if not isinstance(other, self.__class__):
            other = self.__class__(other)
        
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        return self.__class__(new_numerator, new_denominator)

    def __truediv__(self, other: Self) -> Self:
        if not isinstance(other, self.__class__):
            other = self.__class__(other)
        
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator

        return self.__class__(new_numerator, new_denominator)

    def __floordiv__(self, other: Self) -> Self:
        if not isinstance(other, self.__class__):
            other = self.__class__(other)
        
        new_numerator = int(self / other)

        return self.__class__(new_numerator)
    
    def __mod__(self, other: Self) -> Self:
        if not isinstance(other, self.__class__):
            other = self.__class__(other)
        
        new_numerator = self - self // other * other

        return self.__class__(new_numerator)
    
    def __pow__(self, other: Self) -> Self:
        if not isinstance(other, self.__class__):
            other = self.__class__(other)
        
        new_numerator = Decimal((self.numerator ** other.numerator) ** (1 / Decimal(other.denominator)))
        new_denominator = Decimal((self.denominator ** other.numerator) ** (1 / Decimal(other.denominator)))

        return Real(new_numerator / new_denominator)

    def __eq__(self, other: Self) -> Self:
        if not isinstance(other, self.__class__):
            other = self.__class__(other)
        
        return self.__dict__ == other.__dict__

    def __gt__(self, other: Self) -> Self:
        if not isinstance(other, self.__class__):
            other: Self = self.__class__(other)

        return float(self) > float(other)
    
    def __ge__(self, other: Self) -> Self:
        if not isinstance(other, self.__class__):
            other = self.__class__(other)

        return (self == other) or (self > other)

class Real(Number):
    def __init__(self, value: Decimal):
        self.value = Decimal(value)