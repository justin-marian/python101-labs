def calculate_factorial_p(n):
    if n < 0:
        return "N should be greater than 0"
    elif n == 0:
        return 1
    else:
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

# Example usage:
num = 5
print(f"Factorial of {num} (Procedural): {calculate_factorial_p(num)}")

def calculate_factorial_f(n):
    if n < 0:
        return "N should be greater than 0"
    return 1 if n == 0 else n * calculate_factorial_f(n - 1)

# Example usage:
num = 5
print(f"Factorial of {num} (Functional): {calculate_factorial_f(num)}")

class Factorial:
    def __init__(self, number):
        self.number = number

    def calculate(self):
        if self.number < 0:
            return "N should be greater than 0"
        res = 1
        for i in range(1, self.number + 1):
            res *= i
        return res

# Example usage:
num = 5
factorial_obj = Factorial(num)
print(f"Factorial of {num} (OOP): {factorial_obj.calculate()}")

max_value = lambda x, y: x if x > y else y
print(max_value(100, 4))  # Output: 100

values = range(1, 10)
modified_values = list(map(lambda x: x + 10 if x % 2 == 0 else x, values))
print(modified_values)  
# Output: [1, 12, 3, 14, 5, 16, 7, 18, 9]

countries = ["Albania", "Bulgaria", "Romania", "Suedia", "Spania", "Irlanda", "Olanda"]
vowels = ["a", "e", "i", "o", "u"]

filtered_countries = list(filter(lambda x: x[0].lower() not in vowels, countries))
print(filtered_countries)  
# Output: ['Bulgaria', 'Romania', 'Spania']
