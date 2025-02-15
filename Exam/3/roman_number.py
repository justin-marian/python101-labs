#!/usr/bin/python

def construct_roman(num: int) -> str:
    """
    Converts an integer to a Roman numeral.

    :param num: Integer number to convert (1 to 3999).
    :return: Roman numeral as a string.
    """

    # Define Roman numeral mapping in descending order
    roman_numerals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    result = []

    for value, symbol in roman_numerals:
        while num >= value:
            result.append(symbol)
            num -= value

    return "".join(result)

def check_invalid(num) -> bool:
    """
    Validates the input number.

    :param num: Input string to check.
    :return: True if invalid, False otherwise.
    """
    try:
        num = int(num)
        return not (1 <= num <= 3999)
    except ValueError:
        return True  # Not a valid integer

def solve(num):
    """
    Converts a valid integer to a Roman numeral or returns an error message.

    :param num: Input number as string.
    :return: Roman numeral or error message.
    """
    if check_invalid(num):
        return "Invalid input: Enter a number between 1 and 3999."
    return construct_roman(int(num))

if __name__ == '__main__':
    N = input("Enter a number (1-3999): ").strip()
    print(solve(N))
