def is_armstrong(n):
    """
    Returns True if n is an Armstrong number, False otherwise.
    """
    digits = [int(d) for d in str(n)]
    power = len(digits)
    total = sum(d ** power for d in digits)
    return total == n

# User input
num = int(input("Enter a number: "))
if is_armstrong(num):
    print("It's an Armstrong number.")
else:
    print("Not an Armstrong number.")

# Test cases
assert is_armstrong(153) == True
assert is_armstrong(9474) == True
assert is_armstrong(123) == False
