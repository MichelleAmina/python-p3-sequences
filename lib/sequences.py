#!/usr/bin/env python3
"""
def print_fibonacci(length):
    fibonacci_sequence = [0, 1]
    for _ in range(length):
        next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_num)
    return fibonacci_sequence

print(print_fibonacci(10))

"""

def print_fibonacci(length):
    fib_sequence = []
    
    for i in range(length):
        if i == 0 or i == 1:
            fib_sequence.append(i)
        else:
           fib_sequence.append(fib_sequence[i - 2] + fib_sequence[i - 1])   
    print(fib_sequence)
        