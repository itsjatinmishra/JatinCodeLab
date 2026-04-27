def findRelativeRanks(score):
    # Step 1: sort scores in descending order
    sorted_score = sorted(score, reverse=True)

    # Step 2: create hashmap (score → rank/medal)
    rank_map = {}

    for i in range(len(sorted_score)):
        if i == 0:
            rank_map[sorted_score[i]] = "Gold Medal"
        elif i == 1:
            rank_map[sorted_score[i]] = "Silver Medal"
        elif i == 2:
            rank_map[sorted_score[i]] = "Bronze Medal"
        else:
            rank_map[sorted_score[i]] = str(i + 1)

    # Step 3: build result using original order
    result = []
    for s in score:
        result.append(rank_map[s])

    return result


# Example usage
score = [5, 4, 3, 2, 1]
print(findRelativeRanks(score))