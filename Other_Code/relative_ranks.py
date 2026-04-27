score = [5,4,3,2,1]

score.sort(reverse=True)

result = []

rank = 4
for i in range(len(score)):
    if i == 0:
        result.append("Gold Medal")
    elif i == 1:
        result.append("Silver Medal")
    elif i == 2:
        result.append("Bronze Medal")
    else:
        if i > 2:
            result.append(f'{rank}')
            rank += 1

print(result)