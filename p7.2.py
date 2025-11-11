# Fill array with selling prices
selling = [80, 50, 35, 65, 127, 77, 92, 85, 123, 90, 55, 124]

# Find largest, second largest, and smallest prices
def find_elements(arr):
    largest = second_largest = float('-inf')  # Start with small numbers
    smallest = float('inf')  # Start with large number
    
    for price in arr:
        # Check largest and second largest
        if price > largest:
            second_largest = largest
            largest = price
        elif price > second_largest:
            second_largest = price
        
        # Check smallest
        if price < smallest:
            smallest = price
    
    return largest, second_largest, smallest

# Call the function and store results
largest_price, second_largest_price, smallest_price = find_elements(selling)

# Print the results
print("Largest selling price:", largest_price)
print("Second largest selling price:", second_largest_price)
print("Smallest selling price:", smallest_price)
