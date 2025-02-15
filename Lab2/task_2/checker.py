#!/usr/bin/python3

import os
import shutil
from task02 import task

print('****************  TASK 02 STARTED  *********************')

# Create or reset the output directory
output_dir = "tests/out/"
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

# Collect all input files
all_files = [f"tests/in/test_{i}.in" for i in range(1, 6)]

# Process each test file
for index, file in enumerate(all_files, start=1):
    try:
        with open(file, 'r') as f:
            lines = f.read().strip()

        # Convert input string to tuple safely
        elements = eval(lines)  # Use ast.literal_eval() for more security if needed
        result = task(*elements)

        # Write output to corresponding file
        output_file = f"{output_dir}/test_{index}.out"
        with open(output_file, 'w') as g:
            g.write(str(result))

    except Exception as e:
        print(f"Error processing {file}: {e}")

# Compare output with reference files
all_tests_passed = True
for test_case in range(1, 6):
    out_file = f"{output_dir}/test_{test_case}.out"
    ref_file = f"tests/ref/test_{test_case}.ref"

    try:
        with open(out_file, 'r') as out_f, open(ref_file, 'r') as ref_f:
            if out_f.readlines() == ref_f.readlines():
                print(f"TEST {test_case} .............................. PASSED")
            else:
                all_tests_passed = False
                print(f"TEST {test_case} .............................. FAILED")
    except FileNotFoundError:
        all_tests_passed = False
        print(f"TEST {test_case} .............................. MISSING OUTPUT/REFERENCE FILE")

# Final test summary
if all_tests_passed:
    print('**************** TASK 02 COMPLETED *********************')
else:
    print('******************* FAILED TESTS ***********************')
