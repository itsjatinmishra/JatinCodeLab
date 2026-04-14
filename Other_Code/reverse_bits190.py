n = 43261596
res = ''

# Step 1: Convert to binary
while n > 0:
    res = str(n % 2) + res
    n //= 2

# Step 2: Make it 32 bits (add leading zeros)
res = res.zfill(32)

print("32-bit binary:", res)

# Step 3: Reverse binary
binary_val = res[::-1]
print("Reversed:", binary_val)

# Step 4: Convert back to decimal
decimal_val = int(binary_val, 2)
print("Answer:", decimal_val)