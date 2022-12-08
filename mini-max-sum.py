def miniMaxSum(arr):
    total = sum(arr)

    print(total - max(arr), total - min(arr))


arr = list(range(1, 21, 2))
miniMaxSum(arr)