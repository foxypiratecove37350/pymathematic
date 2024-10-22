from functools import lru_cache
from decimal import Decimal

from .constants import *
from .errors import *

type number = int | float | complex
type real = int | float

# Trigonometry

def sin(x: number) -> number:
    """Returns the sine of the given angle in radians."""

    result = (e ** (1j * x) - e ** (-1j * x)) / 2j
    
    if result.real == result:
        result = result.real
        if int(result) == result:
            result = int(result)
    
    return result

def cos(x: number) -> number:
    """Returns the cosine of the given angle in radians."""

    result = (e ** (1j * x) + e ** (-1j * x)) / 2
    
    if result.real == result:
        result = result.real
        if int(result) == result:
            result = int(result)
    
    return result

def tan(x: number) -> number:
    """Returns the tangent of the given angle in radians."""

    return Decimal(str(sin(x))) / Decimal(str(cos(x)))

def csc(x: number) -> number:
    """Returns the cosecant of the given angle in radians."""

    return 1 / Decimal(str(sin(x)))

def sec(x: number) -> number:
    """Returns the secant of the given angle in radians."""

    return 1 / Decimal(str(cos(x)))

def cot(x: number) -> number:
    """Returns the cotangent of the given angle in radians."""

    return Decimal(str(cos(x))) / Decimal(str(sin(x)))

# Prime factorization

def prime_factors(n: int) -> list[int]:
    """Returns a list of prime factors of n"""

    raise InDevError

# Factorial and Primorial

@lru_cache
def factorial(x: int) -> int:
    """Returns the factorial of x"""

    if int(x) != x or x < 0:
        raise PositiveIntegerError
    
    x = int(x)

    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

@lru_cache
def primorial(p: int) -> int:
    """Returns the primorial of p, which is the product of all the primes less or equal to p"""

    raise InDevError

@lru_cache
def gamma(x: number) -> number:
    """Returns the gamma function of x"""

    raise InDevError

# GCD, LCM, ...

def gcd(x: real, y: real) -> int:
    """Returns the greatest common divisor of x and y"""

    x = Decimal(str(x))
    y = Decimal(str(y))

    while y != 0:
        x, y = y, x % y
    
    return float(x)

def lcm(x: real, y: real) -> int:
    """Returns the least common multiple of x and y"""
    
    x = Decimal(str(x))
    y = Decimal(str(y))

    return float((x * y) / gcd(x, y))