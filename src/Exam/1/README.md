# [Py-Hackademy] Fall exam 2023

## 01-converted-numbers

In this problem you will have to form numbers made up of several letters, taking into account the ASCII codes of each character.
Thus, for a list ['a', 'b', 'c'], our number will be equal to the sum of the ASCII codes of the characters in the list (for help check [asciitable.com]<https://www.asciitable.com/>).
**To convert to ASCII code you can use the ord(char) function.**

After forming the respective number, you will have to check *how many times that number is divisible by 2*.
After you have found how many times it is divisible, you will have to *add to l_finala a list element of the form [2, ]*.

Finally, the list l_final will need to be modified so that only the sublists that have the value of the field <de_cate_oli_se_divide_numarul_cu_2> an even value remain in it!
Be careful, odd numbers will not be divisible by 2 and thus you will be tempted to consider the list [2, 0] as well, which is not correct.

### Input Format 1

The reading is done, you do not need to change anything! 3 lines with different ASCII characters are read from the keyboard, and each line is transformed into a list of characters.

### Constraints 1

Only 3 lines will be read from the keyboard.

### Output Format 1

You will need to return the list l_final, which represents a list of lists of the form [2, ].

### Sample Input 1

bd
bdf
bfl

### Sample Output 1

[[2, 2], [2, 2]]

### Explanation 1

the first sublist ['b','d'] will form the number 198 the second sublist ['b','d','f'] will form the number 300 the third sublist ['b','f','l'] will form the number 308
So: 198 is divided by 2 once 300 is divided by 2 twice 308 is divided by 2 twice
l_final at the moment will look like this [[2,1],[2,2],[2,2]]
After filtering the list l_final will look like this [[2,2],[2,2]]