def matchingStrings(stringList, queries):
    # Dictionary to store each word
    words = {}
    # Occurence of each word
    occurence = []

    # Fore each word
    for string in stringList:
        # If word is not in dictionary
        if string not in words:
            # Put it in dictionary and set its occurence to 1
            words[string] = 1
        # If word is in dictionary
        else:
            # Add its value by 1
            words[string] += 1

    # For each query
    for query in queries:
        # If query does not match the word in dictionary
        if query not in words:
            # Set the query occurence to 0
            occurence.append(0)

        # If query does match the word in dictionary
        else:
            # Add the occurence of that query
            occurence.append(words[query])
    
    # Return list of occurence of each query in words dictionary 
    return occurence
