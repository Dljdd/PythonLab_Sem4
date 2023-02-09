#Python Program to Print Fibonacci Series using a Recursive Function

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci(n):
    for i in range(n):
        print(fibonacci(i), end=", ")

# testing
print_fibonacci(10)
fibonacci(10)
