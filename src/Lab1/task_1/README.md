# TASK 01

## Requirement

A professor at the Faculty of Automatics and Computers must create a program that calculates the average grades in the exam for some subjects.
Thus, the function `func(grades, subject_name)` is given. You only have to complete the inside of the function, and the variable `pair` denotes a tuple, which you must create so that it contains a float (i.e. the average grades) and the name of the subject.

## Example

```text
input:
1 2 3 4 5 6 7 8 9 10
SPORT

output:
('5.50', 'SPORT')
```

Explanation: The average of the grades (1 + 2 +...+ 9 + 10) is calculated, which is equal to 5.5 and is concatenated with the subject name ("SPORT") within the `pair` tuple.

## Run | Testing

For testing, you can run the script directly from the IDE or you can run the command in the terminal:

```bash
./checker.py
```

If you cannot run this script due to permissions, use the following command first:

```bash
sudo chmod 700 checker.py
```
