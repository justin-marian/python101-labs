# Bonus

## Requirement

Since it is known that mathematics is the favorite subject of students, this task proposes that you implement a complex number calculation system.
Thus, in order to deepen object-oriented programming, the following methods are desired to be implemented inside the Complex() class:

```python
def __init__(self, real_part: int, imaginary_part: int, var_name: str = 'var') -> None:
def __str__(self) -> str:
def add_complex_numbers(self, other) -> None:
def subtract_complex_numbers(self, other) -> None:
def multiply_complex_numbers(self, other) -> None:
```

For simplicity, the changes produced as a result of the operations performed will be made on the object that calls the respective methods.
i^2 = -1
When calling the \_\_str__ method, we want to display the complex number as accurately as possible, as in the following example:

```text
Let z = x + yi

When displaying:
x = 0 ---> z = yi
y = 0 ---> z = x
x = 0 && y = 0 ---> z = 0
y < 0 ---> z = x - yi
---> not accepted: z = 1 - -2i
```

## Example

```text
a = Complex(1, 2, 'a')
>> "Complex number succesfully created."
b = Complex(0, 2, 'b')
>> "Complex number succesfully created."
print(a)
>> a = 1 + 2i
print(b)
>> b = 2i
a.multiply_complex_numbers(b)
print(a)
>> a = -4 + 2i
print(b)
>> b = 2i
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
