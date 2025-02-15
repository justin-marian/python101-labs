# TASK 02

## Requirement

Ana is a 9th grade student in a mathematics-computer science profile. On the first day of high school, the Headmistress asks Ana to create a table with the last names and first names of her classmates.
To make her work easier, Ana asks you to help her with a program in which you separate the last name from the first name.
Thus, a list of strings is given as input, each string representing the full name of a student. You must separate each name as follows:

## Input

The list of strings `complete_name` is given.

## Output

You must create a tuple `formatted_name`, which contains, as the first element, a list of all the last names, as the second element, a list of the first names and then a list of the other first names.

## Note

All names are of the form:
{`Last_name`} {`First_name #1`}-{`First_name #2`}.

## Example

```text
input:
Popescu Gabriel-Ion

---
Last_name = Popescu
First_name #1 = Gabriel
First_name #2 = Ion
```

## Run | Test

For testing, you can run the script directly from the IDE or you can run the command in the terminal:

```bash
./checker.py
```

If you cannot run this script due to permissions, use the following command first:

```bash
sudo chmod 700 checker.py
```
