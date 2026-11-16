# Question 1 - Functions and Conditionals
# Topic: Temperature Converter
#
# Task 1:
# Write a function called convertTemp that accepts two arguments:
#   - value: a numeric temperature value
#   - unit: a string, either "C" for Celsius or "F" for Fahrenheit
#
# The function should:
#   - Convert Celsius to Fahrenheit if unit is "C"  →  Formula: (value × 9/5) + 32
#   - Convert Fahrenheit to Celsius if unit is "F"  →  Formula: (value − 32) × 5/9
#   - Return -1 if unit is neither "C" nor "F"
#   - Round the result to 2 decimal places before returning


def convertTemp(value, unit):
    # Reject nonnumeric values before performing arithmetic.
    if not isinstance(value, (int, float)):
        return -1

    if unit == "C":
        # Convert the input from Celsius to Fahrenheit.
        result = (value * 9 / 5) + 32
    elif unit == "F":
        # Convert the input from Fahrenheit to Celsius.
        result = (value - 32) * 5 / 9
    else:
        # Reject units other than uppercase C or F.
        return -1

    # Return the converted number rounded to two decimal places.
    return round(result, 2)


# Task 2:
# Call the function with the following inputs and print each result:
#   convertTemp(100, "C")     → Expected: 212.0
#   convertTemp(32, "F")      → Expected: 0.0
#   convertTemp(37, "C")      → Expected: 98.6
#   convertTemp("invalid","X")→ Expected: -1

# Print the returned results for the required examples.
print(convertTemp(100, "C"))
print(convertTemp(32, "F"))
print(convertTemp(37, "C"))
print(convertTemp("invalid", "X"))
