# TASK 01

## Requirement

Gigel started the new programming paradigms course, but he didn't understand the **map** and **filter** functions very well. Therefore, he will need your help with 3 tasks:

* to double all numbers that are divisible by 6, and to triple those that are not;
* convert all vowels in a sentence to uppercase (no need to consider diacritics)
* select only palindromic words from a list (all words are guaranteed to contain only lowercase letters)

## Example

```text
Task 1a
input:
24 3 8 18 9 6 27

output:
48 9 24 36 27 12 81
```

```text
Task 1b
input:
Gigel started to learn

output:
GIgEl STARTED TO LEARN
```

```text
Task 1c
input:
demigod madam python php

output:
madam php
```

Solution hints:

* use lambda functions (with or without if else) or build additional functions
* for if else statements in lambda expressions you can consult the site: <https://thispointer.com/python-how-to-use-if-else-elif-in-lambda-functions/>
* help yourself with a vector/string of vowels for Task 1b

Explanations for the return values ​​in the skeleton:

* after applying the functional, the new result will be of type "function_name object"
* we use list to convert the result returned by the functional into a list
* more details here: <https://www.pythonmorsels.com/map-and-filter-python/>

## Run | Test

For testing, you can run the script directly from the IDE or you can run the command in the terminal:

```bash
./checker.py
```

In case you cannot run this script due to permissions, use the following command first:

```bash
sudo chmod 644 checker.py
```
