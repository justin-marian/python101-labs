# MODULE

## Task 01

The function `random_points(radius, center_x, center_y)` is given, which takes the radius and center of the circle, represented by the coordinate pair `[x_center, y_center]`. The function returns the coordinates of a random point inside the circle.

**You can use the math and random modules.**

*(If you can't remember the math: <https://doubleroot.in/lessons/circle/position-of-a-point/>)*

### Example

```text
input: 1.25 0 3.4
output: 0.48334197442603744 4.286286596848848
```

## Task 02

A PPM (Portable Pix Map) file describes an image in an easy-to-understand form.

The file has 2 components:

**Header:**

- File format *(We will work with ASCII representation, so we will only use P3 for both reading and writing)*
- Number of lines `N`, respectively columns `M` in the body
- Maximum value for colors *(We will use 255)*

**Body:**

- A "matrix" of N lines and M columns of triplets with integer values, which represent the values ​​of the pixels in the RGB channel. *(That is, each pixel will be represented by 3 values: R, G and B. For example, a pixel represented by [255 0 0] will be red)*.

Example:

```text
P3 # file format
3 3 # N x M
255 #maximum color value
# the P3 means colors are in ascii, then 3 columns and 3 rows, then 255 for max color, then RGB triplets
255 0 0 0 255 0 0 0 255
255 255 0 255 255 255 0 0 0
0 255 255 75 75 75 127 127 127
# the first pixel [255 0 0] means RED = 255, GREEN = 0, BLUE = 0. So the pixel is red.
```

**Input files will not contain comments, for ease of reading.**

### Task 02.1

Complete the read function in task02.py.

***HINT: Notice the vstack and hstack functions in the numpy module explained here:*** <https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html>

### Task 02.2

Using the information extracted from the image in the previous point, complete the sepia function, using the formulas:

```text
sepia_r = (int)(0.393*r + 0.769*g + 0.189*b)
sepia_g = (int)(0.349*r + 0.686*g + 0.168*b)
sepia_b = (int)(0.272*r + 0.534*g + 0.131*b)
#r, g and b represent the channels
# don't forget about the case where applying the formula can exceed the maximum value of color
```

For the example given above, the resulting image is:

```text
P3
3 3
255
100 88 69 196 174 136 48 42 33
296 263 205 344 306 238 0 0 0
244 217 169 101 90 70 171 152 118
```

## Run checker

```bash
./checker.py task_number subtask_number
```

The arguments are optional. For a task with several subtasks, it can be checked completely or fragmented:

```bash
./checker.py 2
#task 3 complete
./checker.py 2 1
#task 2 subtask 1
```
