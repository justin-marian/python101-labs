# TASK 04

## Requirement

Since you have just learned the concept of `list comprehension`, this task proposes the following requirement, in which you must create a list with the name `nice_list`, through a single line of code (`one-liner`, which we will discuss in future courses).
This list must contain elements in the form of tuples, like this:

```text
(number, number ^ 2, number ^ 3)
```

Later, these numbers must meet the following conditions:

* number < 100
* the number must belong to the list `given_numbers`, given as a parameter
* the number must be either divisible by 2 or 3

## Input

The list of positive integers, `given_numbers`, is given.

## Output

Save the created list in a list with the name `nice_list`, the list that will later be returned.

## Example

```text
input:
[1, 2, 3, 6, 8, 9, 10, 11, 13, 15, 16, 18, 50, 70, 100, 102, 203]

output:
[(2, 4, 8), (3, 9, 27), (6, 36, 216), (8, 64, 512), (9, 81, 729), (10, 100, 1000), (15, 225, 3375), (16, 256, 4096), (18, 324, 5832), (50, 2500, 125000), (70, 4900, 343000)]
```

## Run | Testing

For testing, you can run the script directly from the IDE or you can run the command in the terminal:

```bash
./checker.py
```

If you cannot run this script due to permissions, use the following command first:

```bash
sudo chmod 700 checker.py
```
