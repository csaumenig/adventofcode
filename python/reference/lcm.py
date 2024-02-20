from functools import reduce

# Taken From:
#   https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-135.php#:~:text=The%20%22lcm()%22%20function%20takes,GCD(a%2C%20b).

# Define a function 'test' that calculates the LCM (Least Common Multiple) of a list of numbers.
def lcm_list(nums):
    # Use the 'reduce' function to apply the 'lcm' function cumulatively to the elements of 'nums'.
    return reduce(lambda x, y: lcm(x, y), nums)


# Define a function 'gcd' that calculates the Greatest Common Divisor (GCD) of two numbers.
def gcd(a, b):
    # Use the Euclidean algorithm to find the GCD of 'a' and 'b'.
    while b:
        a, b = b, a % b
    return a


# Define a function 'lcm' that calculates the Least Common Multiple (LCM) of two numbers.
def lcm(a, b):
    # Calculate the LCM using the formula: LCM(a, b) = (a * b) / GCD(a, b).
    return a * b // gcd(a, b)