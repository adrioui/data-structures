def getMinimumCost(k, c):

    # Sort the price of each flower in decreasing order
    c.sort(reverse=True)
    
    # Set the cost and purchase status to 0
    cost = 0
    previous_purchase = 0

    # For each price of the flower
    for flower_price in c:
        # Add the cost of each flower with original price or not
        cost += flower_price * ((previous_purchase // k) + 1)
        # Track the purchase status
        previous_purchase += 1 
    
    return cost
