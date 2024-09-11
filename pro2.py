#pro2.Print a Fibonacci strings. 
def fibonacci_strings(n):
    if n <= 0:
        return []
    elif n == 1:
        return ['A']
    elif n == 2:
        return ['A', 'B']
    fib_strings = ['A', 'B']
    
    for i in range(2, n):
        next_string = fib_strings[-1] + fib_strings[-2]
        fib_strings.append(next_string)
    
    return fib_strings
num_strings = 5
fib_strings = fibonacci_strings(num_strings)
print(fib_strings)