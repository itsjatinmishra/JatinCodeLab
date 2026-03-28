def roman_to_integer(roman):
    """
    Convert a Roman numeral string into an integer.

    Example:
    roman_to_integer("MDXLIX") -> 1549
    """

    # Dictionary for Roman values
    roman_map = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000,
        "IV": 4, "IX": 9, "XL": 40,
        "XC": 90, "CD": 400, "CM": 900
    }

    total = 0   # Final result
    i = 0       # Pointer to traverse string

    while i < len(roman):

        # Check for 2-character symbols
        if i < len(roman) - 1:
            two_symbols = roman[i:i+2]

            if two_symbols in roman_map:
                total += roman_map[two_symbols]
                i += 2
                continue

        # Otherwise take single character
        total += roman_map[roman[i]]
        i += 1

    return total


# Taking input (correct way)
roman_input = input("Enter the Roman Number Please In String Format: ").upper()
print(f"Your input is: {roman_input}")

# Function call
ans_value = roman_to_integer(roman_input)

# Output
print(f"Roman Value Converted Into Integer and The Answer is: {ans_value}")