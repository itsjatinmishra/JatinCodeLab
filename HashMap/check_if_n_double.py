def checkIfExist(arr):
    seen = set()

    for num in arr:
        if (num * 2 in seen) or (num % 2 == 0 and num // 2 in seen):
            return True

        seen.add(num)

    return False


arr = [10,2,5,3]
print(checkIfExist(arr))