def function_with_uncommon_error(x):
    if x == 0:
        return 0  # Correct handling of x == 0
    else:
        return 1 / x  # Potential ZeroDivisionError if x is very close to zero

# Example usage, demonstrating the bug
result1 = function_with_uncommon_error(0)
print(f"Result 1: {result1}")  # Result 1: 0

result2 = function_with_uncommon_error(1e-100)  # A very small number, close to zero
print(f"Result 2: {result2}")  # Result 2: 1e+100.  This looks correct, but it can be problematic

result3 = function_with_uncommon_error(0.0) # Another test case to check float zero
print(f"Result 3: {result3}") # Result 3: inf or OverflowError