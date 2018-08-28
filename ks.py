print("KnapSack!")

# Weight of Items
w = [3, 9, 2, 1, 7, 3, 11]

# Value of Items
v = [5, 7, 4, 3, 5, 2, 30]

# Weight Capacity of Knapsack
c = 10

# Result Array to store values of index,capacity pair we've found to prevent from repeating the same computation.
# It will print 2D array: An array of 6 arrays each with 10 None's
results = [[None] * c] * (len(w))


# Function knap_sack:
	# Arguments: --indx--Index of current item, --capacity--Weight capacity of knapsack
	# Value: Returns value of best permution of items in knapsack.
def knap_sack(indx, capacity):
	value = None

	# If we found solution before, return it.
	if (indx > 0 and results[indx][capacity]):
		return results[indx][capacity]

	# Indx less than 0 meainig we went through all items
	# Capicity equals 0 meaning ks cannot hold more weight.
	if (indx < 0 or capacity == 0 ):
		value = 0

	# If weight of item exceeds capacity of ks, move on to next item. 	
	elif (w[indx] > capacity):
		value = knap_sack(indx - 1, capacity)

	# Retrieve greatest value between putting item in ks and moving on to next item.
	else:
		# Moving on to next item
		value1 = knap_sack(indx - 1, capacity)

		# Putting item in ks
		value2 = v[indx] + knap_sack(indx - 1, capacity - w[indx]) 

		value = max(value1, value2)


	return value	 	
			

print(knap_sack(6, c - 1))
