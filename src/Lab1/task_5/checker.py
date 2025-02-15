#!/usr/bin/python3

import os
from task05 import zig_zag

# Task 05 Start
print('****************  TASK 05 STARTED  *********************')

# Create output directory if it doesn't exist
output_path = os.path.join(os.getcwd(), "tests/out")
os.makedirs(output_path, exist_ok=True)

# Process test input files
for index in range(1, 6):
    input_file = f"tests/in/test_{index}.in"
    output_file = f"tests/out/test_{index}.out"

    with open(input_file, "r") as f:
        rows, cols = map(int, f.readline().split())

    # Generate zig-zag matrix
    zig_zag_matrix = zig_zag(rows, cols)

    # Write output to file
    with open(output_file, "w") as g:
        g.writelines(f"{row}\n" for row in zig_zag_matrix)

# Validate results
for test_case in range(1, 6):
    out_file = f"tests/out/test_{test_case}.out"
    ref_file = f"tests/ref/test_{test_case}.ref"

    if open(out_file).readlines() == open(ref_file).readlines():
        print(f"TEST {test_case} .............................. PASSED")
    else:
        print(f"TEST {test_case} .............................. FAILED")

print('**************** TASK 05 COMPLETED *********************')
