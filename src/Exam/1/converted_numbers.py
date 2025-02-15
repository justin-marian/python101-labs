def is_even(number: int) -> bool:
    """Check if a number is positive and even."""
    return number > 0 and number % 2 == 0

def count_divisions_by_2(number: int) -> int:
    """Count how many times a number can be divided by 2."""
    count = 0
    while is_even(number):
        count += 1
        number //= 2
    return count

def solve(strings: list) -> list:
    """Process a list of character lists, summing ASCII values and checking divisibility by 2."""
    result = []
    for sublist in strings:
        num_sum = sum(map(ord, sublist))
        divisions = count_divisions_by_2(num_sum)
        if is_even(divisions):
            result.append([2, divisions])
    return result

if __name__ == '__main__':
    l = [list(input().strip()) for _ in range(3)]
    print(solve(l))
