print("KnapSack!")

# Weight of Items
w = [3, 9, 2, 1, 7, 3, 11]

# Value of Items
v = [5, 7, 4, 3, 5, 2, 30]

# Weight Capacity of Knapsack
c = 10

# Result Array to store values of index,capacity pair we've found to prevent from repeating the same computation.
results = []

for i in range(0, len(w)):
	results.append([])

print(results)

# Function knap_sack:
	# Arguments: --indx--Index of current item, --capacity--Weight capacity of knapsack
	# Value: Returns value of best permution of items in knapsack.
def knap_sack(indx, capcity):

