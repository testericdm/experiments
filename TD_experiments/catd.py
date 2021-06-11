from scipy.stats import chi2
import numpy as np

# Standard CATD

# Batch fashion where 20 % of the dataset is used for setting the weights and the rest for testing

def get_weights(vector_counts, errors, alpha):
	weights = []
	length = len(vector_counts)
	for i in range(length):
		N = vector_counts[i]
		error = errors[i]
		numerator = chi2.ppf(alpha, N)
		weights.append( numerator/error)
	return np.array(weights).reshape(length,1)

def aggregate_value(weights_array, value_matrix):
	# comepute dot product and then divide the matrix by sum of weights

	weight_sum = np.sum(weights_array)
	return value_matrix.dot(weights_array)/ weight_sum


def catd_init(train_data, w_num, E, alpha = 0.975):
	zeroOneMat = np.ones((E, w_num))
	zeroOneMat[train_data == 0] = 0

	mean_vals = np.mean(train_data, axis = 1).reshape(E,1)

	squared_errors = (train_data - mean_vals)**2

	sum_squared_errors = np.sum(squared_errors, axis = 0)

	# Get counts where data is not missing
	counts_vector = np.sum(zeroOneMat, axis = 0)

	worker_weights = get_weights(counts_vector, sum_squared_errors, alpha)

	return worker_weights



# Influences confidence value
# alpha = 0.975


# Weights 
# w_num = 5


# data constants

# Num epochs
# E = 50

# # initial worker weights
# worker_weights = np.zeros(w_num)

# # counts 
# worker_counts = np.zeros(w_num) * alpha 

# # erros
# error_counts = np.ones(w_num) * beta

# # results list
# results_list = []

# train_data = np.random.randint(5, size = (E,w_num))

# Find out where the missing data is
# zeroOneMat = np.ones((E, w_num))

# zeroOneMat[train_data == 0] = 0


# Use the train data to compute the weighs of the workers

# First we need to compute the mean of the data values, reshape to make matrix operations easier

# mean_vals = np.mean(train_data, axis = 1).reshape(E,1)

# compute the error of all data values

# squared_errors = (train_data - mean_vals)**2

# sum_squared_errors = np.sum(squared_errors, axis = 0)

# # Get counts where data is not missing
# counts_vector = np.sum(zeroOneMat, axis = 0)

# print(counts_vector)
# print(sum_squared_errors)

# Create a function that takes counts_vector and sum_squared_errors and returns the weights

# def get_weights(vector_counts, errors):
# 	weights = []
# 	length = len(vector_counts)
# 	for i in range(length):
# 		N = vector_counts[i]
# 		error = errors[i]
# 		numerator = chi2.ppf(alpha, N)




# 		weights.append( numerator/error)
# 	return np.array(weights).reshape(length,1)

# def aggregate_value(weights_array, value_matrix):
# 	# comepute dot product and then divide the matrix by sum of weights

# 	weight_sum = np.sum(weights_array)
# 	return value_matrix.dot(weights_array)/ weight_sum


# worker_weights = get_weights(counts_vector, sum_squared_errors)



# Test data is here - reusing train data

# print(aggregate_value(worker_weights, train_data))

# print( np.mean(train_data,axis = 1) )

# print(worker_weights)




# ============================ BEGINNING OF OLD VERSION ===============================================

# from scipy.stats import chi2
# import numpy as np

# # Standard CATD

# # Batch fashion where 20 % of the dataset is used for setting the weights and the rest for testing

# # Influences confidence value
# alpha = 0.975


# # Weights 
# w_num = 5


# # data constants

# # Num epochs
# E = 50

# # # initial worker weights
# # worker_weights = np.zeros(w_num)

# # # counts 
# # worker_counts = np.zeros(w_num) * alpha 

# # # erros
# # error_counts = np.ones(w_num) * beta

# # # results list
# # results_list = []

# train_data = np.random.randint(5, size = (E,w_num))

# # Find out where the missing data is
# zeroOneMat = np.ones((E, w_num))

# zeroOneMat[train_data == 0] = 0


# # Use the train data to compute the weighs of the workers

# # First we need to compute the mean of the data values, reshape to make matrix operations easier

# mean_vals = np.mean(train_data, axis = 1).reshape(E,1)

# # compute the error of all data values

# squared_errors = (train_data - mean_vals)**2

# sum_squared_errors = np.sum(squared_errors, axis = 0)

# # Get counts where data is not missing
# counts_vector = np.sum(zeroOneMat, axis = 0)

# print(counts_vector)
# print(sum_squared_errors)

# # Create a function that takes counts_vector and sum_squared_errors and returns the weights

# def get_weights(vector_counts, errors):
# 	weights = []
# 	length = len(vector_counts)
# 	for i in range(length):
# 		N = vector_counts[i]
# 		error = errors[i]
# 		numerator = chi2.ppf(alpha, N)




# 		weights.append( numerator/error)
# 	return np.array(weights).reshape(length,1)

# def aggregate_value(weights_array, value_matrix):
# 	# comepute dot product and then divide the matrix by sum of weights

# 	weight_sum = np.sum(weights_array)
# 	return value_matrix.dot(weights_array)/ weight_sum


# worker_weights = get_weights(counts_vector, sum_squared_errors)



# # Test data is here - reusing train data

# print(aggregate_value(worker_weights, train_data))

# print( np.mean(train_data,axis = 1) )

# print(worker_weights)

# # df = 55

# # for df in [1000.5]:
# # 	print(chi2.ppf(0.975, df))

# # Number of workers
# # N = 10


# # errors = np.zeros(N)
# # Ns = np.zeros(N)
# # weights = np.zeros(N)

# # dataset = np.ones((N,N))




# # chi2.ppf gives the critical value for the desired probability value and degrees of freedom 


# # In the following, we are checking how well a data with normal distribution effectively captures


# # In the CATD algorithm, a bunch of mean values are computed and the losses are used to tune the 
# # worker weights and they stay the same.


# # When we created the streaming truth discovery algorithm, we are effectively using the idea that worker's
# # reliability does not stay constant over multiple epochs.

# # Apparently, streaming algorithms are evaluated on the following metrics:

# # How many passes?
# # The avaialble memory
# # Running time of algorithm

# # It does not make sense to test CATD vs CATD-DS since they are for different type of data altogether.
# # The idea is that we are utilizing an empirically tested algorithm and extending it to the case of 
# # streaming. Maybe I can compare it with just computing a mean? its not that great but gives an impression.
# # I could also compare it with CATD-standalone where weights are fixed at 10 % of epochs. 





# # The idea is to take a state-of-the-art/good truth discovery algorithm and then make it stremaing compatible
# # through re-design. Since its good, the idea is to  