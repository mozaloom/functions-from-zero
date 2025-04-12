"""Build a calculator module."""
def addition(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def power(x, y):
    """Raise x to the power of y."""
    return x ** y

def square_root(x):
    """Return the square root of x."""
    if x < 0:
        raise ValueError("Cannot take square root of negative number")
    return x ** 0.5

def factorial(n):
    """Return the factorial of n."""
    if n < 0:
        raise ValueError("Cannot take factorial of negative number")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n < 0:
        raise ValueError("Cannot take Fibonacci of negative number")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def gcd(x, y):
    """Return the greatest common divisor of x and y."""
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    """Return the least common multiple of x and y."""
    if x == 0 or y == 0:
        return 0
    return abs(x * y) // gcd(x, y)

def is_prime(n):
    """Check if n is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    """Return the prime factors of n."""
    factors = []
    if n <= 1:
        return factors
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors  

def lcm_of_list(numbers):
    """Return the least common multiple of a list of numbers."""
    if not numbers:
        return 0
    lcm = numbers[0]
    for number in numbers[1:]:
        lcm = lcm * number // gcd(lcm, number)
    return lcm


def is_even(n):
    """Check if n is an even number."""
    return n % 2 == 0

def is_odd(n):
    """Check if n is an odd number."""
    return n % 2 != 0

def is_palindrome(s):
    """Check if s is a palindrome."""
    return s == s[::-1]

def reverse_string(s):
    """Return the reverse of string s."""
    return s[::-1]

def count_vowels(s):
    """Count the number of vowels in string s."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def count_consonants(s):
    """Count the number of consonants in string s."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)