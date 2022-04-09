def factorial(n):
    """
    This function computes the factorial of n using
    a recursive function
    """
    if n == 0:
        return 1
    else:
        prev = n * factorial(n - 1)
        return prev


if __name__ == '__main__':
    print(factorial(9))
