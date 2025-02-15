def func(given_numbers):
    """
    Generate a list of tuples (n, n^2, n^3) for numbers in `given_numbers` that:
    - Are less than 100
    - Are divisible by either 2 or 3
    """
    return [(n, n**2, n**3) for n in given_numbers if n < 100 and (n % 2 == 0 or n % 3 == 0)]
