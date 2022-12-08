arr = [64, 34, 25, 12, 22, 11, 8]

def bubble_sort(arr):

    # Set the counter of swap to non-zero value to begin
    swap_counter = -1

    # Length of the list
    n = len(arr) 

    # Repeat until the swap counter is 0
    if swap_counter != 0:
        
        # Reset the swap counter
        swap_counter = 0

        # Look at each adjacent pair
        for i in range(n - 1):
            for j in range(n - i - 1):
                # If two adjacent elements are not in order, swap them and add one to swap counter
                if arr[j] > arr[j + 1]:
                    swap_counter += 1
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    print(f"Array is sorted in {swap_counter} swaps.")
    print(f"First Element: {arr[0]}")
    print(f"Last Element: {arr[-1]}")

    return