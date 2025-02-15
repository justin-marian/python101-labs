def task1b(phrase):
    """
    Converts all vowels in a given phrase to uppercase.

    Args:
        phrase (str): A string containing the input phrase.

    Returns:
        str: A new string where all vowels (a, e, i, o, u) are converted to uppercase.
    """
    return ''.join([c.upper() if c in 'aeiou' else c for c in phrase])
