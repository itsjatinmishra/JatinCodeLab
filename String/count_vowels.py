def countVowels(demo_str):
    final_str = demo_str.lower()
    count = 0
    for ch in final_str:
        if ch.isalpha() and ch in "aeiou":
            count += 1
    
    return count

print(countVowels("aeiou"))