#!/usr/bin/python3

import os
from task01 import func

# Task 01 Start
print('****************  TASK 01 STARTED  *********************')

# Create output directory if it does not exist
output_dir = os.path.join(os.getcwd(), "tests/out")
os.makedirs(output_dir, exist_ok=True)

# List of input test files
input_files = [f"tests/in/test_{i}.in" for i in range(1, 6)]

# Process each test file
for index, file in enumerate(input_files, start=1):
    try:
        with open(file, "r") as f:
            lines = f.readlines()

        # Read input values
        note = list(map(int, lines[0].split()))
        nume_materie = lines[1].strip()

        # Compute result
        pereche = func(note, nume_materie)
        pereche_remastered = (f"{pereche[0]:.2f}", pereche[1])

        # Write output to file
        output_file = f"tests/out/test_{index}.out"
        with open(output_file, "w") as g:
            g.write(str(pereche_remastered))

    except Exception as e:
        print(f"Error processing {file}: {e}")

# Compare output with reference files
for test_case in range(1, 6):
    out_file = f"tests/out/test_{test_case}.out"
    ref_file = f"tests/ref/test_{test_case}.ref"

    try:
        with open(out_file, "r") as out, open(ref_file, "r") as ref:
            if out.read() == ref.read():
                print(f"TEST {test_case} .............................. PASSED ✅")
            else:
                print(f"TEST {test_case} .............................. FAILED ❌")
    except FileNotFoundError:
        print(f"Missing output or reference file for TEST {test_case} ❌")

print('**************** TASK 01 COMPLETED *********************')
