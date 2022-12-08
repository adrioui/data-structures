from collections import Counter

logo = "aabbbccde"

# Count the occurence of each alphabet in string and assign it to a variable
counters = Counter(logo)
# Sort by value in a decreasing order
counters = sorted(counters.items(), key=lambda x: (x[1] * -1, x[0]))

# For the first 3 values
for i in range(3):
    # Print each alphabet and its occurence
    print(counters[i][0], counters[i][1]) 