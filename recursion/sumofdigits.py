def sum_ofDigits(n):
    """
    Iterative implementation of sum of digits
    """
    total_sum = 0
    assert n >= 0, "Enter a positive number"
    if n == 0:
        return 0
    else:
        for i in str(n):
            total_sum += int(i)
    return total_sum



digits = input('Enter the digits ')
def sumdigits(digits):
    l = len(digits)
    if l == 0:
        return 0
    else:
        return int(digits[0]) + sumdigits(digits[1:])
    
print(sumdigits(digits))
    
# def sum_of_digits(n):
#     """
#     Recursive implementation of sum of digits
#     """
#     assert n >= 0 and int(n) == n, "Enter a positive value"
#     if n == 0:
#         return 0
#     else:
#         return int(n%10) + sum_of_digits(int(n/10))

    

print("Iterative Solution: ", sum_ofDigits(1233099765432345672))
print("Recursive Solution: ", sum_of_digits(1233099765432345672))