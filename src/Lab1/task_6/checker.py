#!/usr/bin/python3

import os
from task06 import func

# Task 06 Start
print('****************  TASK 06 STARTED  *********************')

# Ensure output directory exists
output_path = os.path.join(os.getcwd(), "tests/out")
os.makedirs(output_path, exist_ok=True)

# Collect test input files
test_files = [f"tests/in/test_{i}.in" for i in range(1, 7)]

# 🚀 Run tests
for idx, file in enumerate(test_files, start=1):
    with open(file) as f:
        size = int(f.readline().strip())

    # Generate rhombus pattern
    romb = func(size)

    # Save output
    output_file = f"tests/out/test_{idx}.out"
    with open(output_file, "w") as g:
        g.write(romb)

# Verify outputs
for test_case in range(1, 7):
    out_file = f"tests/out/test_{test_case}.out"
    ref_file = f"tests/ref/test_{test_case}.ref"

    with open(out_file) as out, open(ref_file) as ref:
        if out.readlines() == ref.readlines():
            print(f"TEST {test_case} .............................. PASSED")
        else:
            print(f"TEST {test_case} .............................. FAILED")

print('**************** TASK 06 COMPLETED *********************')
