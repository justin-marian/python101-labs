#!/usr/bin/python3

import os
from task02 import func

# Task 02
print("****************  TASK 02 STARTED  *********************")

# Ensure output directory exists
output_path = os.path.join(os.getcwd(), "tests/out")
os.makedirs(output_path, exist_ok=True)

# Read input file safely
input_file = "tests/in/test.in"
try:
    with open(input_file, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"Error: Input file '{input_file}' not found.")
    exit(1)

# Process input with function
pereche = func(lines)

# Ensure the tuple is in a list-friendly format
pereche_list = list(pereche)

# Trim newlines from elements in the third list
pereche_list[2] = [name.strip() for name in pereche_list[2]]
pereche = tuple(pereche_list)

# Write output file
output_file = "tests/out/test.out"
with open(output_file, "w") as g:
    g.write(f"Nume familie:\n{pereche[0]}\n\n")
    g.write(f"Prenume_1:\n{pereche[1]}\n\n")
    g.write(f"Prenume_2:\n{'\n'.join(pereche[2])}")

# Compare output with reference file
out_file = "tests/out/test.out"
ref_file = "tests/ref/test.ref"

with open(out_file, "r") as f_out, open(ref_file, "r") as f_ref:
    if f_out.readlines() == f_ref.readlines():
        print("TASK 02.............................. PASSED")
    else:
        print("TASK 02.............................. FAILED")

print("**************** TASK 02 COMPLETED *********************")
