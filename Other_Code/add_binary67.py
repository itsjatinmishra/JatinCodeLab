def addBinary(a, b):
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = ""

    while i >= 0 or j >= 0 or carry:
        sum_val = carry

        if i >= 0:
            sum_val += int(a[i])
            i -= 1

        if j >= 0:
            sum_val += int(b[j])
            j -= 1

        result = str(sum_val % 2) + result
        carry = sum_val // 2

    return result

print(addBinary("11", "1"))      # Output: "100"
print(addBinary("1010", "1011")) # Output: "10101"