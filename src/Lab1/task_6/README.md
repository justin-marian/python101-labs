# TASK 06

## Requirement

For this task, you have to create a code that will practically "draw" a rhombus.
The edges of the rhombus will be made up of the `@` character, while the inside will be represented by '`.`' (dot).
The size parameter is given, which signifies the number of lines of the rhombus. It should be noted that for any size = 2n and size = 2n + 1, the resulting rhombuses look the same, in order to keep the symmetry intact. Thus, the rhombus for size = 4 looks the same as the one for size = 5, and so on.
The rhombus must be created inside the string "rhombus", where each line can be separated by the '`\n`' character.

## Observations

The longest line (the middle of the rhombus) is glued to the left edge, meaning there are no empty spaces until the first edge encountered.

* size >= 1

## Example #1

```text
input:
n = 6 || n = 7

output:
@@
@..@
@....@
@......@
@....@
@..@
@..@
@@
```

## Example #2

```text
input:
n = 10 || n = 11

output:
@@
@..@
@....@
@......@
@........@
@..........@
@........@
@......@
@....@
@..@
@@
```

## Run | Test

For testing, you can run the script directly from the IDE or you can run the command in the terminal:

./checker.py

If you cannot run this script due to permissions, use the following command first:

sudo chmod 700 checker.py
