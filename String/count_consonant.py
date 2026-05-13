def count_consonants(demo_str):
    count = 0

    for ch in demo_str.lower():
        if ch.isalpha() and ch not in "aeiou":
            count += 1

    return count


# Example
text = "abcdefg"

result = count_consonants(text)

print("Total consonants:", result)