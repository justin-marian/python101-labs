def func(size):
    """
    Generates a rhombus pattern using '@' and '.' characters.

    The rhombus is symmetrical around its center and consists of three main parts:
    - Upper half: Rows decrease in width as they approach the middle row.
    - Middle row: The widest row, containing the most dots.
    - Lower half: A mirror reflection of the upper half.

    Parameters:
    size (int): The total number of rows in the rhombus.

    Returns:
    str: A string representation of the rhombus pattern.
    """

    romb = ''

    for i in range(size + 1):
        # Upper half of the rhombus (before the middle row)
        if i < size // 2:
            spaces = size // 2 - i  # Leading spaces for centering
            dots = i * 2  # Number of dots between '@' symbols
            romb += ' ' * spaces + '@' + '.' * dots + '@' + '\n'

        # Middle row (widest row)
        elif i == size // 2:
            dots = (size // 2) * 2  # Maximum number of dots in the middle row
            romb += '@' + '.' * dots + '@' + '\n'

        # Lower half of the rhombus (mirroring the upper half)
        elif i > size // 2 and i < size:
            spaces = i - size // 2  # Leading spaces for centering
            dots = size - spaces * 2 if size % 2 == 0 else size - spaces * 2 - 1
            romb += ' ' * spaces + '@' + '.' * dots + '@' + '\n'
    
    # Special case: For even-sized rhombus, add a final row
    if size % 2 == 0:
        romb += ' ' * (size // 2) + '@@' + '\n'

    return romb
