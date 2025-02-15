# [Py-Hackademy] Fall exam 2023

## 03-roman-numbers

In Roman numeral representation, numbers are made up of 7 symbols: **I**, **V**, **X**, **L**, **C**, **D** and **M**, as represented below:

```text
Symbol Value
I 1
V 5
X 10
L 50
C 100
D 500
M 1000
```

For example, 2 is represented as II in Roman numerals (2 Roman 1 digits concatenated).

Roman numerals are represented from highest to lowest value, from left to right, with the following specifications:

- I placed before V (5) and X (10) forms 4 and 9, respectively.
- X placed before L (50) and C (100) forms 40 and 90, respectively.
- C placed before D (500) and M (1000) forms 400 and 900, respectively.

Convert a given number in Arabic representation to its Roman numeral representation.
If the number is not in the corresponding Arabic numeral representation, "Invalid input" will be returned.

### Input Format 3

String -> num

### Constraints 3

**Warning! num can be of any type and can take any value** from *input() -> num must respect: -> num = int -> 1 <= num <= 3999*

### Output Format 3

String -> number in roman numerals

### Sample Input 3.1

string

### Sample Output 3.1

Invalid input

### Sample Input 3.2

"14"

### Sample Output 3.2

Invalid input

### Sample Input 3.3

1999

### Sample Output 3.3

MCMXCIX

### Sample Input 3.4

1547

### Sample Output 3.4

MDXLVII
