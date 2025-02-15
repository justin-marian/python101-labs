def task1c(words):
    """
    Identifies and returns a list of palindrome words.

    Args:
        words (list[str]): List of words to check.

    Returns:
        list[str]: List of words that are palindromes.
    """    
    # Alternative Imperative approach (More explicit)
    # palindromes = []
    # for word in words:
    #     word_cleaned = word.lower().replace(" ", "")  # Normalize input (if needed)
    #     if word_cleaned == word_cleaned[::-1]:
    #         palindromes.append(word)
    return [word for word in words if word == word[::-1]]
