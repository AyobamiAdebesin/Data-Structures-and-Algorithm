# Created by Ayobami Adebesin
"""
    Compute the Fibonacci sequence recursively
    f(n) = f(n-1) + f(n-2) for all n=2,3,4, ......

    Step 1: Define the recursive case
    f(n) = f(n-1) + f(n-2)

    Step 2: Define the base condition
    f(0) = 0
    f(1) = 1

    Step 3: Check for negative or fractional values
    fibonnaci(-1)
    fibonnaci(2.5)
"""
def fibonacci(n):
    assert n >= 0 and int(n) == n  , "n must be greater than zero"
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fib_seq = []
if __name__ == "__main__":
    for i in range(10):
        fib_seq.append(fibonacci(i))
print(fib_seq)


