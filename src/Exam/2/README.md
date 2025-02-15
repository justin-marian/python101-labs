# [Py-Hackademy] Fall Exam 2023

## 02-zig-zag

In World War II, the English generals had to come up with their own way of encrypting messages so that they could not be interpreted by the German army.
Thus, they came up with the idea of ​​encrypting their messages written in zigzag on a varying number of lines.
The character string "GIGELMERGE" can be written in zigzag on several lines as follows:

```text
G L G
I E M R E
G E
```

and it is read "GLGIEMREGE". The army asks you to encrypt the message when receiving a message in the form of a character string and a number of lines.

**Warning! You must return the encrypted message as a string on a line, not as a "zigzag", but the order is that of Zig Zag.**

### Input Format 2

-> message: string representing the message to be encrypted -> numRows: number of rows to encrypt the message on

## Constraints 2

-> 1 <= len(message) <= 1000 -> message contains letters of the alphabet and the character "." -> 2 <= numRows <= 1000

## Output format 2

-> A string representing the encrypted message

### Input sample 2.1

BUNA ZIUA
3
Sample output 0

HOELL

### Input sample 2.2

THEQUICKBROWNFOXJUMPSOVERTHELAZYCÂINE
3

### Output sample 2.2

TUBNJSRLDHQIKRWFXUPOETEAYOECOOMVHZG
