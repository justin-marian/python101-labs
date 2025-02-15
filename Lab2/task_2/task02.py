def task(*args):
    """
    Filters elements from the given arguments based on specific conditions.

    Parameters:
    args -> tuple: A collection of elements of different types.

    Returns:
    list: A list containing:
        - All integers (excluding booleans)
        - Single lowercase consonants
    """

    result = []

    for arg in args:
        if isinstance(arg, int) and not isinstance(arg, bool):
            result.append(arg)
        elif isinstance(arg, str) and len(arg) == 1 and arg.islower() and arg.isalpha():
            if arg not in {'a', 'e', 'i', 'o', 'u'}:  # Exclude vowels
                result.append(arg)

    return result
