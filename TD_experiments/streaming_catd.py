from scipy.stats import chi2
import numpy as np

# In the following, we are going to implement the algorithm re-designed 

# Helper Functions
def aggregate_value(weights_array, value_array):
	# print(weights_array)
	return weights_array.dot(value_array)/sum(weights_array)

def streaming_catd_init(train_data,  w_num, E ,alpha = 0.975, decay = 0.95):

	results = []
	# initial worker weights
	worker_weights = np.ones(w_num)

	# counts 
	worker_counts = np.ones(w_num) 

	# erros
	error_counts = np.ones(w_num) 

	first_iter = True

	for row in train_data:

		if first_iter:
			agg_val = np.mean(row)
			first_iter = False

		else:
			agg_val = aggregate_value(worker_weights, row)


		# print(agg_val)
		results.append(agg_val)

		# perform a weight update

		# Check if value is provided (here 0 == Nan value) by worker

		for i in range(len(row)):
			# get value at 
			if row[i] == 0:
				worker_counts[i] = worker_counts[i]*decay
				error_counts[i] = error_counts[i]*decay
			else:
				worker_counts[i] = 1 + worker_counts[i]*decay
				error_counts[i] = (row[i] - agg_val)**2 + error_counts[i]*decay

		# Once the counts and etc have been updated, compute the new weights

		for i in range(len(worker_weights)):
			worker_weights[i] = chi2.ppf(alpha, worker_counts[i])/error_counts[i]


	return np.array(results)





# # Influences confidence value
# alpha = 0.975
# decay = 0.95

# # Weights 
# w_num = 5


# # initial worker weights
# worker_weights = np.ones(w_num)

# # counts 
# worker_counts = np.ones(w_num) 

# # erros
# error_counts = np.ones(w_num) 

# # data constants

# # Num epochs
# E = 50






# Create dataset 
# train_data = np.random.randint(5, size = (E,w_num))

# first_iter = True

# for row in train_data:

# 	if first_iter:
# 		agg_val = np.mean(row)
# 		first_iter = False

# 	else:
# 		agg_val = aggregate_value(worker_weights, row)


# 	# print(agg_val)

# 	# perform a weight update

# 	# Check if value is provided (here 0 == Nan value) by worker

# 	for i in range(len(row)):
# 		# get value at 
# 		if row[i] == 0:
# 			worker_counts[i] = worker_counts[i]*decay
# 			error_counts[i] = error_counts[i]*decay
# 		else:
# 			worker_counts[i] = 1 + worker_counts[i]*decay
# 			error_counts[i] = (row[i] - agg_val)**2 + error_counts[i]*decay

# 	# Once the counts and etc have been updated, compute the new weights

# 	for i in range(len(worker_weights)):
# 		worker_weights[i] = chi2.ppf(alpha, worker_counts[i])/error_counts[i]


# 	print(worker_weights)

# =========================== Backup file follows ==============

# from scipy.stats import chi2
# import numpy as np

# # In the following, we are going to implement the algorithm re-designed 

# # Influences confidence value
# alpha = 0.975
# decay = 0.95

# # Weights 
# w_num = 5


# # initial worker weights
# worker_weights = np.ones(w_num)

# # counts 
# worker_counts = np.ones(w_num) 

# # erros
# error_counts = np.ones(w_num) 

# # data constants

# # Num epochs
# E = 50

# # Helper Functions
# def aggregate_value(weights_array, value_array):
# 	# print(weights_array)
# 	return weights_array.dot(value_array)




# # Create dataset 
# train_data = np.random.randint(5, size = (E,w_num))

# first_iter = True

# for row in train_data:

# 	if first_iter:
# 		agg_val = np.mean(row)
# 		first_iter = False

# 	else:
# 		agg_val = aggregate_value(worker_weights, row)


# 	# print(agg_val)

# 	# perform a weight update

# 	# Check if value is provided (here 0 == Nan value) by worker

# 	for i in range(len(row)):
# 		# get value at 
# 		if row[i] == 0:
# 			worker_counts[i] = worker_counts[i]*decay
# 			error_counts[i] = error_counts[i]*decay
# 		else:
# 			worker_counts[i] = 1 + worker_counts[i]*decay
# 			error_counts[i] = (row[i] - agg_val)**2 + error_counts[i]*decay

# 	# Once the counts and etc have been updated, compute the new weights

# 	for i in range(len(worker_weights)):
# 		worker_weights[i] = chi2.ppf(alpha, worker_counts[i])/error_counts[i]


# 	print(worker_weights)










