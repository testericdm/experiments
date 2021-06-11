import numpy as np

# In the following I will create the TruthFinder Algorithm


# train_data = np.load("data_matrix.dat", allow_pickle = True)


def index_return(index_val, row):
	distances = np.argsort(abs(row - index_val))
	furthest_index = distances[-1]
	closest_index = distances[1]

	return furthest_index, closest_index

# Create a Function
def Truth_Finder(train_data,  w_num, E, rho = 0.3, gamma = 0.8, t0 = 0.7):
	zeroOneMat = np.ones((E, w_num))
	zeroOneMat[train_data == 0] = 0

	# Initialize worker weights to default value 
	worker_weights = np.ones(w_num)* t0

	worker_trustwortiness_scores = - np.log(np.ones(w_num) - worker_weights)

	# Create the fact confidence score matrix:
	fact_confidence_scores = np.zeros((E, w_num))

		# Just to check correctness
	count = 0
	# iterate over each row:
	for row in train_data:
		# iterate over each value:
		for i in range(w_num):
			val = row[i]
			# only do the following for fact/answer provided
			if val != 0:

				temp_confidence_val = worker_trustwortiness_scores[i]
				
				
				# iterate over all the other row values

				for j in range(1,w_num):
					index_of_curval = (i + j)% w_num

					# Here check if the values are same, in which case, the confidence value is multipled as required!
					if val == row[j]:
						temp_confidence_val += worker_trustwortiness_scores[index_of_curval]

					# print((i + j)% w_num)
					

				furthest, closest = index_return(i, row)

				# add t-score of closest score
				temp_confidence_val += rho*worker_trustwortiness_scores[closest]

				# reduce t-score of closets score
				temp_confidence_val -= rho*worker_trustwortiness_scores[furthest]

				fact_confidence_scores[count][i] = temp_confidence_val
		# print("At row: ", count)

		count += 1


	# Convert fact_confidence scores to an update of worker weights

	# print(fact_confidence_scores)

	# print(np.sum(fact_confidence_scores, axis = 0))



	confidence_values = 1/(1 + np.exp((- gamma*fact_confidence_scores)))
	# confidence_values[confidence_values == 0.5]  = 0 
	# print(confidence_values)

	new_weights = np.sum(confidence_values, axis = 0) / np.sum(zeroOneMat, axis = 0)
	length = len(new_weights)

	return new_weights.reshape(length,1)

# tf_weights = tf.Truth_Finder(data, 100, 100)
# results_tf = data.dot(tf_weights)/(np.sum(tf_weights))

# # Basic constants


# w_num = 100
# t0 = 0.7
# E = 100
# rho = 0.3 # hyper parameter that control how similarity is impacted
# gamma = 0.8
# # First is the data, we have a simple experiemnt with 3 workers, therefore the data is a Ex3 matrix 

# # train_data = np.random.randint(30, size = (E,w_num))
# print(train_data)

# # Create a matrix that captures all facts submitted, aka, its a 0-1 matrix where
# # 0 indicates no fact submitted 
# # 1 indicates a value/fact submitted by worker

# zeroOneMat = np.ones((E, w_num))

# zeroOneMat[train_data == 0] = 0

# # print(zeroOneMat)
# # NOTE: All values of zero will be considered missing values for this synthetic dataset

# # initialize weight vector to the same value:
# worker_weights = np.ones(w_num)* t0

# # Computing worker trustworthiness scores: = - ln(1 - worker_weight)
# worker_trustwortiness_scores = - np.log(np.ones(w_num) - worker_weights)
# # have to get the confidence scores of all facts, 
# # each fact is potentially related to its related facts (same row/object/epoch)

# # Compute fact confidence 

# # Come up with a similarity function which does the following:

# # ascribes -1 for value that is further away vs +1 for value that is closer. 
# # Hyperparameter chosen will be small to ensure it doenst impact it too much.

# # take a value and the row and compute the absolute distances between them
# # Return index of value furthest away and index of value closets
# # Closest one will get +1 and the furthest one will get -1





# # Create the fact confidence score matrix:
# fact_confidence_scores = np.zeros((E, w_num))


# # Just to check correctness
# count = 0
# # iterate over each row:
# for row in train_data:
# 	# iterate over each value:
# 	for i in range(w_num):
# 		val = row[i]
# 		# only do the following for fact/answer provided
# 		if val != 0:

# 			temp_confidence_val = worker_trustwortiness_scores[i]
			
			
# 			# iterate over all the other row values

# 			for j in range(1,w_num):
# 				index_of_curval = (i + j)% w_num

# 				# Here check if the values are same, in which case, the confidence value is multipled as required!
# 				if val == row[j]:
# 					temp_confidence_val += worker_trustwortiness_scores[index_of_curval]

# 				# print((i + j)% w_num)
				

# 			furthest, closest = index_return(i, row)

# 			# add t-score of closest score
# 			temp_confidence_val += rho*worker_trustwortiness_scores[closest]

# 			# reduce t-score of closets score
# 			temp_confidence_val -= rho*worker_trustwortiness_scores[furthest]

# 			fact_confidence_scores[count][i] = temp_confidence_val
# 	# print("At row: ", count)

# 	count += 1


# # Convert fact_confidence scores to an update of worker weights

# # print(fact_confidence_scores)

# # print(np.sum(fact_confidence_scores, axis = 0))



# confidence_values = 1/(1 + np.exp((- gamma*fact_confidence_scores)))
# # confidence_values[confidence_values == 0.5]  = 0 
# # print(confidence_values)

# new_truths = np.sum(confidence_values, axis = 0) / np.sum(zeroOneMat, axis = 0)
# # Note: Every submitted value (other than 0, since its basically Nan) is a fact that has a confidence associated with it

# # check if there are duplicates in the array 
# print(new_truths)



# # ========================= THE FOLLOWING IS A BACKUP ==========

# import numpy as np

# # In the following I will create the TruthFinder Algorithm


# # Basic constants

# w_num = 5
# t0 = 0.5
# E = 50
# rho = 0.3 # hyper parameter that control how similarity is impacted
# gamma = 0.8
# # First is the data, we have a simple experiemnt with 3 workers, therefore the data is a Ex3 matrix 

# train_data = np.random.randint(30, size = (E,w_num))
# print(train_data)

# # Create a matrix that captures all facts submitted, aka, its a 0-1 matrix where
# # 0 indicates no fact submitted 
# # 1 indicates a value/fact submitted by worker

# zeroOneMat = np.ones((E, w_num))

# zeroOneMat[train_data == 0] = 0

# # print(zeroOneMat)
# # NOTE: All values of zero will be considered missing values for this synthetic dataset

# # initialize weight vector to the same value:
# worker_weights = np.ones(w_num)* t0

# # Computing worker trustworthiness scores: = - ln(1 - worker_weight)
# worker_trustwortiness_scores = - np.log(np.ones(w_num) - worker_weights)
# # have to get the confidence scores of all facts, 
# # each fact is potentially related to its related facts (same row/object/epoch)

# # Compute fact confidence 

# # Come up with a similarity function which does the following:

# # ascribes -1 for value that is further away vs +1 for value that is closer. 
# # Hyperparameter chosen will be small to ensure it doenst impact it too much.

# # take a value and the row and compute the absolute distances between them
# # Return index of value furthest away and index of value closets
# # Closest one will get +1 and the furthest one will get -1

# def index_return(index_val, row):
# 	distances = np.argsort(abs(row - index_val))
# 	furthest_index = distances[-1]
# 	closest_index = distances[1]

# 	return furthest_index, closest_index



# # Create the fact confidence score matrix:
# fact_confidence_scores = np.zeros((E, w_num))


# # Just to check correctness
# count = 0
# # iterate over each row:
# for row in train_data:
# 	# iterate over each value:
# 	for i in range(w_num):
# 		val = row[i]
# 		# only do the following for fact/answer provided
# 		if val != 0:

# 			temp_confidence_val = worker_trustwortiness_scores[i]
			
			
# 			# iterate over all the other row values

# 			for j in range(1,w_num):
# 				index_of_curval = (i + j)% w_num

# 				# Here check if the values are same, in which case, the confidence value is multipled as required!
# 				if val == row[j]:
# 					temp_confidence_val += worker_trustwortiness_scores[index_of_curval]

# 				# print((i + j)% w_num)
				

# 			furthest, closest = index_return(i, row)

# 			# add t-score of closest score
# 			temp_confidence_val += rho*worker_trustwortiness_scores[closest]

# 			# reduce t-score of closets score
# 			temp_confidence_val -= rho*worker_trustwortiness_scores[furthest]

# 			fact_confidence_scores[count][i] = temp_confidence_val
# 	# print("At row: ", count)

# 	count += 1


# # Convert fact_confidence scores to an update of worker weights

# # print(fact_confidence_scores)

# # print(np.sum(fact_confidence_scores, axis = 0))



# confidence_values = 1/(1 + np.exp((- gamma*fact_confidence_scores)))
# confidence_values[confidence_values == 0.5]  = 0 
# # print(confidence_values)

# new_truths = np.sum(confidence_values, axis = 0) / np.sum(zeroOneMat, axis = 0)
# # Note: Every submitted value (other than 0, since its basically Nan) is a fact that has a confidence associated with it

# # check if there are duplicates in the array 
# print(new_truths)


