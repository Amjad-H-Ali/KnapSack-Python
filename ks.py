print("KnapSack!")

# Weight of Items
w = [3, 9, 2, 1, 7, 3, 11]

# Value of Items
v = [5, 7, 4, 3, 5, 2, 30]

# Weight Capacity of Knapsack
c = 10


# Function knap_sack:
	# Arguments: --indx--Index of current item, --capacity--Weight capacity of knapsack
	# Value: Returns value of best permution of items in knapsack.
def knap_sack(indx, capcity):
