def miniMaxSum(arr):
    total = sum(arr)

    print(total - max(arr), total - min(arr))

miniMaxSum(list(range(10)))