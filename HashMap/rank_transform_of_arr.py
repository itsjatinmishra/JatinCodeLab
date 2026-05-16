def arrayRankTransform(arr):
    sort_arr = sorted(set(arr))

    demo_rank = {}

    num = 1
    for i in sort_arr:
        demo_rank[i] = num
        num += 1

    result = []

    for i in arr:
        result.append(demo_rank[i])

    return result

arr = [40,30,10,20]
arr02 = [100,100,100]
print(arrayRankTransform(arr02))