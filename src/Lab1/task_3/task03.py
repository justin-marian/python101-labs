def func(string_message):
    """ 
    Encodes a given string message by mapping each letter to its position in the alphabet.
    
    - 'A' → 1, 'B' → 2, ..., 'Z' → 26
    - Spaces ' ' are encoded as '0'.
    
    **Examples:**
    "HELLO WORLD" → "851212150 231518124"
    
    HINTS:
    - `ord(char) - 64` gives the index for uppercase letters ('A' = 65 in ASCII).
    - Spaces (' ') are replaced with '0'.
    """
    
    # List comprehension for efficiency
    encoded_message = ''.join(
        '0' if char == ' ' else str(ord(char) - 64)
        for char in string_message.upper()  # Ensures input is uppercase
    )

    return encoded_message
