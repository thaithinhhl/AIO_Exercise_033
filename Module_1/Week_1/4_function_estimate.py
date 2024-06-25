import math


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def approx_sin(x, n):
    result = 0
    for i in range(n):
        result += ((-1)**i * x**(2*i + 1)) / factorial(2*i + 1)
    return result


def approx_cos(x, n):
    result = 0
    for i in range(n):
        result += ((-1)**i * x**(2*i)) / factorial(2*i)
    return result


def approx_sinh(x, n):
    result = 0
    for i in range(n):
        result += (x**(2*i + 1)) / factorial(2*i + 1)
    return result


def approx_cosh(x, n):
    result = 0
    for i in range(n):
        result += (x**(2*i)) / factorial(2*i)
    return result


# Example usage
print(f"approx_sin(x=3.14, n=10) = {approx_sin(3.14, 10)}")
print(f"approx_cos(x=3.14, n=10) = {approx_cos(3.14, 10)}")
print(f"approx_sinh(x=3.14, n=10) = {approx_sinh(3.14, 10)}")
print(f"approx_cosh(x=3.14, n=10) = {approx_cosh(3.14, 10)}")
