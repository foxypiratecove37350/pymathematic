from typing import Any, Callable, Self
from dataclasses import dataclass
import math

from .errors import *
from .functions import *

@dataclass
class NaturalInteger:
    value: int

    def __init__(self, value: int) -> None:
        if value < 0 or int(value) != float(value):
            raise ValueError("x must be a positive integer")

        self.value = int(value)

@dataclass
class RelativeInteger:
    value: int

@dataclass
class Decimal:
    value: float

@dataclass
class Rational:
    numerator: int
    denominator: int = 1

    def __init__(self, numerator: int, denominator: int = 1) -> None:
        numerator = float(numerator)
        denominator = float(denominator)

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

    def _simplify(self) -> None:
        _gcd = gcd(self.numerator, self.denominator)
        self.numerator //= _gcd
        self.denominator //= _gcd
    
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
        
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator

        return self.__class__(new_numerator, new_denominator)