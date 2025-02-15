#!/usr/bin/python3

import sys
from task01 import task01 as t1
from task02 import task02 as t2


def check_task1():
    """Tests Task 1 - Random points inside a circle."""
    print('****************  TASK 01 STARTED  *********************')

    for i in range(1, 11):
        filename = f"task01/tests/in/{i}.in"
        try:
            with open(filename, 'r') as file:
                radius, x, y = map(float, file.readline().split())

            x_res, y_res = t1.random_points(radius, x, y)

            if (x_res - x) ** 2 + (y_res - y) ** 2 <= radius ** 2:
                print(f"TEST {i} .............................. PASSED")
            else:
                print(f"TEST {i} .............................. FAILED")
        except Exception as e:
            print(f"TEST {i} .............................. ERROR: {e}")


def check_task_2_1():
    """Tests Task 2.1 - Reading PPM files."""
    print('****************  TASK 02.1 STARTED  *********************')

    for i in range(1, 11):
        filename = f"task02/tests/in/{i}.ppm"
        try:
            image = t2.Image()
            image.read(filename)

            with open(filename, 'r') as file:
                original_content = file.read().strip()

            if str(image).strip() == original_content:
                print(f"TEST {i} .............................. PASSED")
            else:
                print(f"TEST {i} .............................. FAILED")
        except Exception as e:
            print(f"TEST {i} .............................. ERROR: {e}")


def check_task_2_2():
    """Tests Task 2.2 - Applying Sepia Filter & Writing PPM Files."""
    print('****************  TASK 02.2 STARTED  *********************')

    for i in range(1, 11):
        input_filename = f"task02/tests/in/{i}.ppm"
        output_filename = f"task02/tests/out/{i}.ppm"
        ref_filename = f"task02/tests/ref/{i}.ppm"

        try:
            image = t2.Image()
            image.read(input_filename)
            image.sepia()
            image.write(output_filename)

            with open(output_filename, 'r') as output_file, open(ref_filename, 'r') as ref_file:
                if output_file.readlines() == ref_file.readlines():
                    print(f"TEST {i} .............................. PASSED")
                else:
                    print(f"TEST {i} .............................. FAILED")
        except Exception as e:
            print(f"TEST {i} .............................. ERROR: {e}")


def main():
    """Main function to execute tasks based on command-line arguments."""
    if len(sys.argv) == 1:
        check_task1()
        check_task_2_1()
        check_task_2_2()
    elif len(sys.argv) == 2:
        if sys.argv[1] == "1":
            check_task1()
        elif sys.argv[1] == "2":
            check_task_2_1()
            check_task_2_2()
        else:
            print("Invalid argument! Use '1' for Task 1, '2' for Task 2.")
    elif len(sys.argv) == 3 and sys.argv[1] == "2":
        if sys.argv[2] == "1":
            check_task_2_1()
        elif sys.argv[2] == "2":
            check_task_2_2()
        else:
            print("Invalid argument! Use '2 1' or '2 2'.")
    else:
        print("Invalid arguments! Usage: script.py [task_number] [subtask_number]")

if __name__ == "__main__":
    main()
