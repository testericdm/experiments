# Dynamic Truth Discovery Algorithm - from Paper: "On the Discovery of Evolving Truth"
import numpy as np


def dyna_TD(train_data,  w_num, E ,theta = 1, alpha = 1, beta = 1, lambda_val = 0.95, decay = 0.95):

	# initial worker weights - set all worker weights to 0.5
	worker_weights = np.ones(w_num)*0.5

	# counts 
	worker_counts = np.ones(w_num) * alpha 

	# erros
	error_counts = np.ones(w_num) * beta

	# A new set of weights and etc 
	worker_weights_decay = np.ones(w_num)*0.5

	# counts 
	worker_counts_decay = np.ones(w_num) * alpha 

	# erros
	error_counts_decay = np.ones(w_num) * beta

	# results list
	results_list = []

	# results list for smoothing
	results_list_smoothing = []

	# Results of decay
	results_list_decay = []

	# Results of all concepts applied
	results_list_ALL = []

	# get Data Shape
	r,c = train_data.shape
	previous_agg_val = 0
	previous_agg_val_ALL = 0
	for i in range(r):
		# get row:
		row = train_data[i]
		if i == 0:
			# Compute mean to start off the process
			agg_value = np.mean(row)
			agg_value_smooth = agg_value
			previous_agg_val = agg_value

			agg_value_decay = agg_value
			# For all the concepts combined (ALL) values
			agg_value_all = agg_value
			previous_agg_val_ALL = agg_value

		else:

			agg_value = aggregate_value(worker_weights, row)
			agg_value_smooth = aggregate_value_smoothing(worker_weights, row, previous_agg_val, lambda_val)
			agg_value_decay = aggregate_value(worker_weights_decay, row)

			previous_agg_val = agg_value_smooth

			agg_value_all = aggregate_value_smoothing(worker_weights_decay, row, previous_agg_val_ALL, lambda_val)
			previous_agg_val_ALL = agg_value_all

		results_list.append(agg_value)
		results_list_smoothing.append(agg_value_smooth)
		results_list_decay.append(agg_value_decay)
		results_list_ALL.append(agg_value_all)
		# results_list_ALL.append()
		# Perform weights update step

		worker_weights,worker_counts, error_counts = weight_update(worker_weights,worker_counts,error_counts, row, theta)
		worker_weights_decay,worker_counts_decay, error_counts_decay = weight_update_decay(worker_weights_decay,worker_counts_decay,error_counts_decay, row, theta, decay)

		# print(agg_value, "Comapres with the other value as: " ,np.mean(row))

	return np.array(results_list), np.array(results_list_smoothing), np.array(results_list_decay), np.array(results_list_ALL)





# # Hyper-parameters
# theta = 1
# # Influences the count value
# alpha = 1
# # starting error 
# beta = 1


# # Weights 
# w_num = 5


# # data constants

# # Num epochs
# E = 50

# ============= Values that exist ========= #

# initial worker weights
# worker_weights = np.zeros(w_num)

# # counts 
# worker_counts = np.zeros(w_num) * alpha 

# # erros
# error_counts = np.ones(w_num) * beta

# # results list
# results_list = []

def aggregate_value(weights_array, value_array):
	dot_prod = weights_array.dot(value_array) 
	# print(dot_prod, "and ", np.sum(weights_array))
	# print(dot_prod/np.sum(weights_array))

	return dot_prod/np.sum(weights_array)

def aggregate_value_smoothing(weights_array, value_array, prev_value, lam_val):
	dot_prod = weights_array.dot(value_array) 
	# print(dot_prod, "and ", np.sum(weights_array))
	# print(dot_prod/np.sum(weights_array))

	return (dot_prod + lam_val*prev_value)/(np.sum(weights_array) + lam_val)

def weight_update(weights_array, worker_counts, error_counts ,value_array, theta):
	new_worker_counts = worker_counts + 1

	# get aggregated value
	agg_val = aggregate_value(weights_array,value_array)

	# use aggregated value to compute error values
	temp_worker_errors = (value_array - agg_val)**2

	# add these errors to error_counts using hyperparameter theta
	new_error_counts = temp_worker_errors + (error_counts*theta)

	# update worker weights 
	weights_array = new_worker_counts/new_error_counts

	return weights_array, new_worker_counts, new_error_counts

def weight_update_decay(weights_array, worker_counts, error_counts ,value_array, theta, decay):
	new_worker_counts = decay * (worker_counts + 1)

	# get aggregated value
	agg_val = aggregate_value(weights_array,value_array)

	# use aggregated value to compute error values
	temp_worker_errors = decay* ((value_array - agg_val)**2)

	# add these errors to error_counts using hyperparameter theta
	new_error_counts = temp_worker_errors + (error_counts*theta)

	# update worker weights 
	weights_array = new_worker_counts/new_error_counts

	return weights_array, new_worker_counts, new_error_counts

# Algorithm flow/ experimentation (with random data)

# train_data = np.random.randint(5, size = (50,5))

# print(dyna_TD(train_data,5,50))

# print(np.mean(train_data, axis = 1))
# # get Data Shape
# r,c = train_data.shape

# for i in range(r):
# 	# get row:
# 	row = train_data[i]
# 	if i == 0:
# 		# Compute mean to start off the process
# 		agg_value = np.mean(row)

# 	else:

# 		agg_value = aggregate_value(worker_weights, row)

# 	results_list.append(agg_value)
# 	# Perform weights update step

# 	worker_weights,worker_counts, error_counts = weight_update(worker_weights,worker_counts,error_counts, row)

# 	print(agg_value, "Comapres with the other value as: " ,np.mean(row))











# ====================== REST IS BACKUP CODE =============

# # Dynamic Truth Discovery Algorithm - from Paper: "On the Discovery of Evolving Truth"
# import numpy as np

# # Hyper-parameters
# theta = 1
# # Influences the count value
# alpha = 1
# # starting error 
# beta = 1


# # Weights 
# w_num = 5


# # data constants

# # Num epochs
# E = 50

# # ============= Values that exist ========= #

# # initial worker weights
# worker_weights = np.zeros(w_num)

# # counts 
# worker_counts = np.zeros(w_num) * alpha 

# # erros
# error_counts = np.ones(w_num) * beta

# # results list
# results_list = []

# def aggregate_value(weights_array, value_array):
# 	# print(weights_array)
# 	return weights_array.dot(value_array)

# def weight_update(weights_array, worker_counts, error_counts ,value_array):
# 	new_worker_counts = worker_counts + 1

# 	# get aggregated value
# 	agg_val = aggregate_value(weights_array,value_array)

# 	# use aggregated value to compute error values
# 	temp_worker_errors = (value_array - agg_value)**2

# 	# add these errors to error_counts using hyperparameter theta
# 	new_error_counts = temp_worker_errors + (error_counts*theta)

# 	# update worker weights 
# 	weights_array = new_worker_counts/new_error_counts

# 	return weights_array, new_worker_counts, new_error_counts


# # Algorithm flow/ experimentation (with random data)

# train_data = np.random.randint(5, size = (E,w_num))

# # get Data Shape
# r,c = train_data.shape

# for i in range(r):
# 	# get row:
# 	row = train_data[i]
# 	if i == 0:
# 		# Compute mean to start off the process
# 		agg_value = np.mean(row)

# 	else:

# 		agg_value = aggregate_value(worker_weights, row)

# 	results_list.append(agg_value)
# 	# Perform weights update step

# 	worker_weights,worker_counts, error_counts = weight_update(worker_weights,worker_counts,error_counts, row)

# 	print(agg_value, "Comapres with the other value as: " ,np.mean(row))










