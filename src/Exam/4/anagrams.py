#!/usr/bin/python

from collections import Counter

def anagram(str1: str, str2: str) -> bool:
    """
    Checks if two strings are anagrams.

    :param str1: First input string.
    :param str2: Second input string.
    :return: True if anagrams, False otherwise.
    """
    return Counter(str1) == Counter(str2)

# Alternative one-liner:
# def anagram(str1, str2): return sorted(str1) == sorted(str2)

if __name__ == "__main__":
    str1 = input("Enter first string: ").strip()
    str2 = input("Enter second string: ").strip()

    print("Anagram" if anagram(str1, str2) else "Not an Anagram")
