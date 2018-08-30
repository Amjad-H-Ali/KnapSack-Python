print("KnapSack!")

# Weight of Items
w = [3, 9, 2, 1, 7, 3, 11]

# Value of Items
v = [5, 7, 4, 3, 5, 2, 30]

# Weight Capacity of Knapsack
cap = 10

# Dict to store values from output of function to prevent computing same input
# results = {
# 	0:{0:None, 1:None, ...}
#	...
# }
results = { i:{j: None for j in range(cap + 1)} for i in range(len(w)) }



# Function knap_sack:
	# Arguments: --indx--Index of current item, --capacity--Weight capacity of knapsack
	# Value: Returns value of best permution of items in knapsack.
def knap_sack(indx, capacity):
	value = None

	# If we found solution before, return it.
	if (indx >= 0 and results[indx][capacity]):
		return results[indx][capacity]

	# Indx less than 0 meainig we went through all items
	# Capicity equals 0 meaning ks cannot hold more weight.
	if (indx == -1 or capacity == 0 ):
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

	# Before returning, store value in Dict to prevent redundancy.
	if(indx >= 0 ):
		results[indx][capacity] = value
	return value	 	
			

print(knap_sack(6, cap))

