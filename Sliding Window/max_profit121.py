def maxProfit(prices):
    # Step 1: Assume first price is the minimum buying price
    min_buy = prices[0]

    # Step 2: Initially, profit is 0
    profit = 0

    # Step 3: Loop through all prices
    for i in range(len(prices)):

        # Step 4: If we find a smaller price, update min_buy
        if prices[i] < min_buy:
            min_buy = prices[i]

        # Step 5: Calculate profit if we sell today
        current_profit = prices[i] - min_buy

        # Step 6: Update maximum profit
        profit = max(profit, current_profit)

    # Step 7: Return final maximum profit
    return profit


# Example input
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))