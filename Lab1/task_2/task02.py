def func(nume_complete: list) -> tuple:
    """
    Processes a list of full names and extracts:
    - Family names
    - First given names
    - Second given names (after hyphen)

    Returns a tuple (nume_familie, prenume_1, prenume_2):
    - nume_familie (list): Last names
    - prenume_1 (list): First given names
    - prenume_2 (list): Second given names

    Expected name format: "Nume_familie Prenume#1-Prenume#2"
    """

    nume_formatat = ([], [], [])

    for full_name in nume_complete:
        # Validate input format
        name_parts = full_name.strip().split(' ')
        if len(name_parts) < 2:
            continue  # Skip malformed entries

        last_name = name_parts[0]
        given_names = name_parts[1].split("-")

        # Ensure at least two given names exist
        if len(given_names) < 2:
            continue  # Skip malformed names

        nume_formatat[0].append(last_name)
        nume_formatat[1].append(given_names[0])
        nume_formatat[2].append(given_names[1])

    return tuple(nume_formatat)
