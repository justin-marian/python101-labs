def task(register):
    """
    Extracts the names of students with an average grade of at least 8.50.

    Parameters:
    register -> dict: A dictionary where:
        - Keys are student names (str).
        - Values are lists of grades (list of floats/integers).

    Returns:
    list: A list of student names who have an average grade >= 8.50.
    """

    return [student for student, grades in register.items() if sum(grades) / len(grades) >= 8.50]
