#!/usr/bin/python3

import os
from task04 import func

# Task 04 Start
print('****************  TASK 04 STARTED  *********************')

# Define the output directory and create it if it doesn't exist
output_dir = os.path.join(os.getcwd(), "tests/out")
os.makedirs(output_dir, exist_ok=True)

# Define test input files
test_files = [f"tests/in/test_{i}.in" for i in range(1, 4)]

# Process each input file
for idx, file in enumerate(test_files, start=1):
    with open(file) as f:
        given_numbers_string = f.readline().strip()

    # Convert the string representation of the list to an actual list of integers
    given_numbers = list(map(int, given_numbers_string.strip("[]").split(",")))

    # Process input through function
    nice_list = func(given_numbers)

    # Write output
    output_file = f"tests/out/test_{idx}.out"
    with open(output_file, "w") as g:
        g.write(str(nice_list))

# Validate output against reference files
for idx in range(1, 4):
    out_file = f"tests/out/test_{idx}.out"
    ref_file = f"tests/ref/test_{idx}.ref"

    # Read and compare file contents
    with open(out_file) as out_f, open(ref_file) as ref_f:
        if out_f.readlines() == ref_f.readlines():
            print(f"TEST {idx}.............................. PASSED")
        else:
            print(f"TEST {idx}.............................. FAILED")

print('**************** TASK 04 COMPLETED *********************')
