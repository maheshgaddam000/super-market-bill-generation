

mart_name = input("Enter the mart name:")


# Define the prices of each item in a dictionary
prices = {"Rice":200, "sugar":40, "Jaggery":45, "corn powder":30, "Boost":200, "Horlics":150, "magie":20, "silk ":170,}

# make a list available on market
list = '''
Rice          200 rs
sugar         40 rs
jaggery       45 rs
corn powder   30 rs
Boost         200 rs
Horlics       150 rs
magie         20 rs
silk          170 rs
'''
print(list)


# Initialize the total cost to zero
total_cost = 0.0

# Get the number of items from the user
num_items = int(input("How many items are you purchasing? "))

# Loop through each item
for i in range(num_items):
    # Get the item name and quantity from the user
    item_name = input("Enter the name of item {}: ".format(i+1))
    item_qty = int(input("Enter the quantity of item {}: ".format(i+1)))
    
    # Calculate the cost of the item
    item_cost = prices.get(item_name, 0.0) * item_qty
    
    # Add the cost of the item to the total cost
    total_cost += item_cost

# Display the total cost to the user
print("Total cost: RS %.2f" % total_cost)

print(" THANK YOU FOR VISITING ")