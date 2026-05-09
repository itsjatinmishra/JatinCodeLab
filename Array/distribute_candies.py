def distributeCandies(candyType):
    unique = set()

    # Add unique candy types
    for candy in candyType:
        unique.add(candy)

    # Sister can eat only half of the candies
    diet = len(candyType) // 2

    # Return minimum value
    if len(unique) < diet:
        return len(unique)
    else:
        return diet


# Function Calls
print(distributeCandies([1, 1, 2, 2, 3, 3]))
print(distributeCandies([6, 6, 6, 6]))