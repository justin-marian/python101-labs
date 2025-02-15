# TASK 03

## Requirement

Gigel and his brother want to communicate without their parents understanding what they are talking about. Thus, they thought of a method of encoding messages.
The first rule is that each message contains only capital letters and blank spaces. Subsequently, the encoding will consist of creating a program in which a message is created consisting of numbers, where each number represents the index of the respective letter in the alphabet. For space, the number '0' will be written.

## Input

Give the string (message to be encoded) `string_message`.

## Output

Save the encoded message in a string `encoded_message`.

## Explanation

A B C D E F G H I
| | | | | | | | | | |
1 2 3 4 5 6 7 0 8 9

For A -alphabet index = 1
B -alphabet index = 2
C -alphabet index = 3
.............
Z -alphabet index = 26
and for ' ' -encoding = 0

## Example

input:
ANA DOES NOT HAVE AN APPLE

output:
114101421011850135185

## Run | Test

For testing, you can run the script directly from the IDE or you can run the command in the terminal:

```bash
./checker.py
```

If you cannot run this script due to permissions, use the following command first:

```bash
sudo chmod 700 checker.py
```
