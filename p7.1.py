# fill array with the stock prices provided
stock = [22.2, 22.7, 23.5, 22.8, 24.3, 25.6]

# Calculate sum and average of an array
def sum_and_average(arr):
    total = 0
    for price in arr:
        total += price  # Add each stock price together to get total
    average = total / len(arr)  # Divide total by number of stocks to get average
    return total, average

# Call the function and store results
total_sum, average_price = sum_and_average(stock)

# Print the results
print("Sum of stock prices:", total_sum)
print("Average stock price:", average_price)
