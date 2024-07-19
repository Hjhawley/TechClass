# Recursion

# Recursion is when a function calls itself in order to solve a problem.
# It allows the function to be repeated several times as it calls itself.

# A recursive function generally has two parts:
# 1. Base case: The condition under which the function stops calling itself.
# 2. Recursive case: The part where the function calls itself as needed.

# Example: Factorial Calculation
# The factorial of a non-negative integer n is the product of all positive
# integers less than or equal to n. It's written as (n!) and is defined as:
# n! = n * (n-1) * (n-2) * ... * 1
# For example, 5! = 5 * 4 * 3 * 2 * 1 = 120

# Factorial using recursion
def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Testing the factorial function
print("5! =", factorial(5))  # Output: 120

# Explanation:
# factorial(5) -> 5 * factorial(4)
# factorial(4) -> 4 * factorial(3)
# factorial(3) -> 3 * factorial(2)
# factorial(2) -> 2 * factorial(1)
# factorial(1) -> 1 (base case)
# Now, the calls return in reverse order:
# 2 * 1 = 2
# 3 * 2 = 6
# 4 * 6 = 24
# 5 * 24 = 120

# Another Example: Fibonacci Series
# The Fibonacci sequence is a series of numbers where each number is the
# sum of the two preceding numbers.
# The sequence starts with 0 and 1:
# 0, 1, 1, 2, 3, 5, 8, 13, ...

# Fibonacci using recursion
def fibonacci(n):
    # Base cases: if n is 0 or 1, return n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: sum of the two preceding Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Testing the Fibonacci function
print(fibonacci(7))  # Output: 13

# Explanation:
# fibonacci(7) -> fibonacci(6) + fibonacci(5)
# fibonacci(6) -> fibonacci(5) + fibonacci(4)
# fibonacci(5) -> fibonacci(4) + fibonacci(3)
# fibonacci(4) -> fibonacci(3) + fibonacci(2)
# fibonacci(3) -> fibonacci(2) + fibonacci(1)
# fibonacci(2) -> fibonacci(1) + fibonacci(0)
# fibonacci(1) -> 1 (base case)
# fibonacci(0) -> 0 (base case)
# Now, the calls return in reverse order:
# fibonacci(2) -> 1 + 0 = 1
# fibonacci(3) -> 1 + 1 = 2
# fibonacci(4) -> 2 + 1 = 3
# fibonacci(5) -> 3 + 2 = 5
# fibonacci(6) -> 5 + 3 = 8
# fibonacci(7) -> 8 + 5 = 13

# Recursion is a powerful tool, but it must be used carefully. 
# Every recursive function must have a base case that eventually stops the recursion, 
# otherwise, it will result in infinite recursion and a stack overflow error.
