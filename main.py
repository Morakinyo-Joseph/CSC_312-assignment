def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def prime_factors_descending(num):
    stack = []
    factors = prime_factors(num)
    for factor in factors:
        if is_prime(factor):
            stack.append(factor)
    stack.sort(reverse=True)
    while stack:
        print(stack.pop())

# Input a positive integer
number = int(input("Enter a positive integer: "))
if number > 0:
    print(f"Prime factors of {number} in descending order:")
    prime_factors_descending(number)
else:
    print("Please enter a positive integer.")
