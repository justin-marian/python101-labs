def zig_zag(rows, cols):
    """
    Generates a zig-zag pattern matrix (rows x cols).
    The pattern alternates between left-to-right (→) and right-to-left (←).

    :param rows: Number of rows in the matrix
    :param cols: Number of columns in the matrix
    :return: A 2D list representing the zig-zag matrix
    """
    zig_zag_matrix = []

    for i in range(rows):
        row = []

        for j in range(cols):
            
            # Left to right (→) and Right to left (←)
            if i % (2 * (cols - 1)) == j or (i + j) % (2 * (cols - 1)) == 0:
                row.append(1)
            else:
                row.append(0)

        zig_zag_matrix.append(row)

    return zig_zag_matrix
