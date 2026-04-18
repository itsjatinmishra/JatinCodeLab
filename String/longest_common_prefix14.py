strs = ["flower","flow","flight","abc"]

first_str = strs[0]

i = 1


while i < len(strs):
    while strs[i].find(first_str) != 0: #check prefix match
        first_str = first_str[:-1]
        if first_str == "":
            print("")
    i += 1

print(first_str)