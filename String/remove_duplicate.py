# ======================================
# REMOVE DUPLICATES FROM STRING
# ======================================

demo_str = "helloo"


# ======================================
# METHOD 1 : Using Set
# ======================================

seen = set()

for ch in demo_str:
    seen.add(ch)

print("Method 1:", seen)



# ======================================
# METHOD 2 : Using String
# ======================================

result = ""

for ch in demo_str:
    if ch not in result:
        result += ch

print("Method 2:", result)



# ======================================
# METHOD 3 : Two Pointer Method
# ======================================

list_str = list(demo_str)

i = 0

for j in range(1, len(list_str)):

    if list_str[i] != list_str[j]:

        i += 1
        list_str[i] = list_str[j]

print("Method 3:", "".join(list_str[:i+1]))