Fibonacci numbers
=================

Write an assembly language function to compute numbers in the
Fibonacci sequence. The function will take a single parameter and
return a single result. You should write your code to closely mimic
the following pseudocode:

```
def fibonacci(n):
    a = 1
    b = 1
    i = 2
    do {
        temp = a + b
        a = b
        b = temp
        i = i + 1
    } while i < n

    return b
```
