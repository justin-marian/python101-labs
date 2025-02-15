#!/usr/bin/python3

import os
import shutil
from task01a import task1a
from task01b import task1b
from task01c import task1c


def setup_output_dir(task_nr):
    """
    Creates or resets the output directory for a specific task.

    Args:
        task_nr (str): Task identifier ('a', 'b', or 'c').
    """
    output_path = f"tests/task01{task_nr}/out/"
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    os.makedirs(output_path)


def compare_output_with_reference(task_nr):
    """
    Compares generated output files with reference files for correctness.

    Args:
        task_nr (str): Task identifier ('a', 'b', or 'c').
    """
    all_passed = True

    for test_case in range(1, 6):
        out_file = f"tests/task01{task_nr}/out/test_{test_case}.out"
        ref_file = f"tests/task01{task_nr}/ref/test_{test_case}.ref"

        try:
            with open(out_file, 'r') as out_f, open(ref_file, 'r') as ref_f:
                if out_f.read().strip() == ref_f.read().strip():
                    print(f"TEST {test_case} .............................. PASSED")
                else:
                    print(f"TEST {test_case} .............................. FAILED")
                    all_passed = False
        except FileNotFoundError:
            print(f"TEST {test_case} .............................. MISSING FILE")
            all_passed = False

    print(f"TASK 01{task_nr} {'COMPLETED' if all_passed else 'FAILED SOME TESTS'}\n")


def run_task(task_nr, function, process_input):
    """
    Runs a specific task by reading inputs, processing data, and writing outputs.

    Args:
        task_nr (str): Task identifier ('a', 'b', or 'c').
        function (callable): Function to process the input.
        process_input (callable): Prepares input data for processing.
    """
    setup_output_dir(task_nr)
    print(f"TASK 01{task_nr} STARTED")

    for index in range(1, 6):
        input_file = f"tests/task01{task_nr}/in/test_{index}.in"
        output_file = f"tests/task01{task_nr}/out/test_{index}.out"

        try:
            with open(input_file, 'r') as f:
                input_data = f.read().strip()

            result = function(process_input(input_data))

            with open(output_file, 'w') as g:
                g.write(" ".join(map(str, result)) if isinstance(result, list) else str(result))

        except Exception as e:
            print(f" Error processing test {index}: {e}")

    compare_output_with_reference(task_nr)


# Task 01a: Number Processing
run_task("a", task1a, lambda x: list(map(int, x.split())))

# Task 01b: Text Processing
run_task("b", task1b, lambda x: x)

# Task 01c: Word Processing
run_task("c", task1c, lambda x: x.split())
