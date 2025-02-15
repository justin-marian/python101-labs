#!/usr/bin/python3

import os
import sys

# Define paths
TEST_INPUT_DIR = "tests/in"
TEST_OUTPUT_DIR = "tests/out"
TEST_REF_DIR = "tests/ref"

print("****************  TASK 01 STARTED  *********************")

# Create output directory if it doesn't exist
os.makedirs(TEST_OUTPUT_DIR, exist_ok=True)

# Collect test input files
test_files = [f"{TEST_INPUT_DIR}/test_{i}.in" for i in range(1, 6)]

original_stdout = sys.stdout

for index, test_file in enumerate(test_files, start=1):
    temp_output = f"{TEST_OUTPUT_DIR}/tmp_{index}.out"
    final_output = f"{TEST_OUTPUT_DIR}/test_{index}.out"

    try:
        with open(test_file, 'r') as f:
            script_content = f.read()

        # Redirect output and execute the script
        sys.stdout = open(temp_output, 'w')
        exec(script_content)
        sys.stdout.close()

        # Restore stdout
        sys.stdout = original_stdout

        # Move final output to test results
        os.rename(temp_output, final_output)

    except Exception as e:
        sys.stdout = original_stdout
        print(f"❌ ERROR running test {index}: {e}")

# Compare test outputs with reference outputs
for test_case in range(1, 6):
    out_file = f"{TEST_OUTPUT_DIR}/test_{test_case}.out"
    ref_file = f"{TEST_REF_DIR}/test_{test_case}.ref"

    try:
        with open(out_file, 'r') as f_out, open(ref_file, 'r') as f_ref:
            out_content = f_out.readlines()
            ref_content = f_ref.readlines()

        if out_content == ref_content:
            print(f"TEST {test_case} .............................. PASSED")
        else:
            print(f"TEST {test_case} .............................. FAILED")

    except FileNotFoundError:
        print(f"TEST {test_case} .............................. MISSING OUTPUT FILE")

print("**************** TASK 01 COMPLETED *********************")
