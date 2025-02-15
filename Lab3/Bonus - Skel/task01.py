class Complex:
    def __init__(self, real_part: int = 0, imaginary_part: int = 0, var_name: str = 'var') -> None:
        self.real = real_part
        self.imaginary = imaginary_part
        self.var_name = var_name

    def __str__(self) -> str:
        """Returns the complex number as a formatted string."""
        if self.real == 0 and self.imaginary == 0:
            return f"{self.var_name} = 0"
        elif self.real == 0:
            return f"{self.var_name} = {self.imaginary}i"
        elif self.imaginary == 0:
            return f"{self.var_name} = {self.real}"
        elif self.imaginary < 0:
            return f"{self.var_name} = {self.real} - {-self.imaginary}i"
        else:
            return f"{self.var_name} = {self.real} + {self.imaginary}i"

    def __add__(self, other: "Complex") -> "Complex":
        """Returns a new Complex number after addition."""
        return Complex(self.real + other.real, self.imaginary + other.imaginary, var_name=f"({self.var_name} + {other.var_name})")

    def __sub__(self, other: "Complex") -> "Complex":
        """Returns a new Complex number after subtraction."""
        return Complex(self.real - other.real, self.imaginary - other.imaginary, var_name=f"({self.var_name} - {other.var_name})")

    def __mul__(self, other: "Complex") -> "Complex":
        """Returns a new Complex number after multiplication."""
        real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary_part = (self.real * other.imaginary) + (self.imaginary * other.real)
        return Complex(real_part, imaginary_part, var_name=f"({self.var_name} * {other.var_name})")

    def __eq__(self, other: "Complex") -> bool:
        """Checks if two complex numbers are equal."""
        return self.real == other.real and self.imaginary == other.imaginary

# Example Usage
if __name__ == "__main__":
    c1 = Complex(3, 2, "c1")
    c2 = Complex(1, -4, "c2")

    print(c1)  # Output: c1 = 3 + 2i
    print(c2)  # Output: c2 = 1 - 4i

    c3 = c1 + c2
    print(c3)  # Output: (c1 + c2) = 4 - 2i

    c4 = c1 - c2
    print(c4)  # Output: (c1 - c2) = 2 + 6i

    c5 = c1 * c2
    print(c5)  # Output: (c1 * c2) = 11 - 10i

    print(c1 == c2)  # Output: False
