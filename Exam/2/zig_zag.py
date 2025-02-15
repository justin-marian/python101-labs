#!/usr/bin/python

def convert_zigzag(message: str, numRows: int) -> str:
    """
    Encrypts a message in a zigzag pattern over numRows rows.

    :param message: The input string to be encrypted.
    :param numRows: The number of rows in the zigzag pattern.
    :return: The zigzag-transformed message as a string.
    """

    # If only one row is specified, return the message as is
    if numRows == 1 or numRows >= len(message):
        return message

    # Initialize the zigzag rows
    rows = [[] for _ in range(numRows)]
    direction_down = False
    row = 0

    for char in message:
        rows[row].append(char)

        # Reverse direction at the top or bottom
        if row == 0 or row == numRows - 1:
            direction_down = not direction_down

        # Move up or down the rows
        row += 1 if direction_down else -1

    # Flatten the list of lists and return the joined string
    return ''.join(''.join(row) for row in rows)

if __name__ == '__main__':
    message = input("Enter the message: ").strip()
    numRows = int(input("Enter the number of rows: "))

    if numRows < 1:
        print("Error: The number of rows must be at least 1.")
    else:
        encrypted_message = convert_zigzag(message, numRows)
        print("Encrypted message:", encrypted_message)
