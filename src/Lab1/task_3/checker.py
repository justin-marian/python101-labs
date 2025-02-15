#!/usr/bin/python3

import os
from task03 import func

# Task 03 Start
print('****************  TASK 03 STARTED  *********************')

# Ensure output directory exists
output_path = os.path.join(os.getcwd(), "tests/out")
os.makedirs(output_path, exist_ok=True)

try:
    # Read input file
    with open("tests/in/test.in", "r") as f:
        decoded_message = f.readline().strip()  # Read first line & remove extra spaces

    # Encode message using func()
    coded_message = func(decoded_message)

    # Write output to file
    output_file = os.path.join(output_path, "test.out")
    with open(output_file, "w") as g:
        g.write(coded_message)

    # Compare generated output with reference file
    ref_file = "tests/ref/test.ref"
    with open(output_file, "r") as out_f, open(ref_file, "r") as ref_f:
        if out_f.readlines() == ref_f.readlines():
            print("TASK 03.............................. PASSED")
        else:
            print("TASK 03.............................. FAILED")

except FileNotFoundError as e:
    print(f"Error: {e} - Check if 'test.in' or reference file exists.")

except Exception as e:
    print(f"Unexpected Error: {e}")

print('**************** TASK 03 COMPLETED *********************')
