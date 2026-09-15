# lumpo_stdlib/math.py - math module for lumpo
import math as _math


def sqrt(x):
    return _math.sqrt(x)


def pow(x, y):
    result = _math.pow(x, y)
    # return int when both inputs are ints (matches `2 ** 10 == 1024`)
    if isinstance(x, int) and isinstance(y, int) and result.is_integer():
        return int(result)
    return result


def floor(x):
    return _math.floor(x)


def ceil(x):
    return _math.ceil(x)


def round(x, digits=0):
    """round to given decimal places (default 0)"""
    if digits == 0:
        return int(_math.floor(x + 0.5))
    factor = _math.pow(10, digits)
    return _math.floor(x * factor + 0.5) / factor


def abs_(x):
    return abs(x)


def sin(x):
    return _math.sin(x)


def cos(x):
    return _math.cos(x)


def tan(x):
    return _math.tan(x)


def log(x, base=None):
    if base is None:
        return _math.log(x)
    return _math.log(x, base)


def exp(x):
    return _math.exp(x)


PI = _math.pi
E = _math.e
