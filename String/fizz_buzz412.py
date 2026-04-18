# Function to perform FizzBuzz
def fizzBuzz(n):
    # Create an empty list to store results
    result = []

    # Loop from 0 to n-1
    for i in range(n):
        
        # Convert index to actual number (1 to n)
        value = i + 1

        # Check if divisible by both 3 and 5 (must be first)
        if value % 3 == 0 and value % 5 == 0:
            result.append("FizzBuzz")

        # Check if divisible by 3
        elif value % 3 == 0:
            result.append("Fizz")

        # Check if divisible by 5
        elif value % 5 == 0:
            result.append("Buzz")

        # If not divisible by 3 or 5
        else:
            result.append(str(value))  # convert number to string

    # Return final list
    return result


# ---- Input & Output ----

# Take input from user
n = int(input("Enter the value of n: "))

# Call function and print result
print(fizzBuzz(n))