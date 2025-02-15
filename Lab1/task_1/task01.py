def func(note, nume_materie):
    """
    Computes the average of a list of grades and returns a tuple (average, subject_name).
    
    Parameters:
    - note (list of int/float): List of grades.
    - nume_materie (str): The subject name.

    Returns:
    - tuple: (average grade as a float, subject name)
    """
    
    # Ensure that 'note' is a non-empty list
    if not note or not all(isinstance(n, (int, float)) for n in note):
        return (0.00, nume_materie)  # Default if the input is invalid
    
    # Compute the average rounded to 2 decimal places
    average = round(sum(note) / len(note), 2)

    return (average, nume_materie)
