def sum_ofDigits(n):
    """
    Iterative implementation of sum of digits
    """
    sum = 0
    assert n >= 0, "Enter a positive number"
    if n == 0:
        return 0
    else:
        for i in str(n):
            sum += int(i)
    return sum
    
def sum_of_digits(n):
    """
    Recursive implementation of sum of digits
    """
    assert n >= 0 and int(n) == n, "Enter a positive value"
    if n == 0:
        return 0
    else:
        return int(n%10) + sum_of_digits(int(n/10))

    

print("Iterative Solution: ", sum_ofDigits(1233099765432345671))
print("Recursive Solution: ", sum_of_digits(1233099765432345671))
