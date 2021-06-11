import numpy as np 


# def get_weights(vector_counts, errors, alpha):
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


# def catd_init(train_data, w_num, E, alpha = 0.975):
# 	zeroOneMat = np.ones((E, w_num))
# 	zeroOneMat[train_data == 0] = 0

# 	mean_vals = np.mean(train_data, axis = 1).reshape(E,1)

# 	squared_errors = (train_data - mean_vals)**2

# 	sum_squared_errors = np.sum(squared_errors, axis = 0)

# 	# Get counts where data is not missing
# 	counts_vector = np.sum(zeroOneMat, axis = 0)

# 	worker_weights = get_weights(counts_vector, sum_squared_errors, alpha)

# 	return worker_weights

def crh_init(train_data, w_num, E, t_iters):

	for i in range(t_iters):
		if i == 0:
			mean_vals = np.mean(train_data, axis = 1).reshape(E,1)

			squared_errors = (train_data - mean_vals)**2

			sum_squared_errors = np.sum(squared_errors)

			worker_errors = np.sum(squared_errors, axis = 0)

			worker_weights = np.log(sum_squared_errors/worker_errors)

			# Reshape weights 
			worker_weights = worker_weights.reshape(w_num,1)

			# Now have to calcualte the new truths 
			new_truths = (train_data.dot(worker_weights)/(np.sum(worker_weights))).reshape(E,1)

		else:

			squared_errors = (train_data - new_truths)**2

			sum_squared_errors = np.sum(squared_errors)

			worker_errors = np.sum(squared_errors, axis = 0)

			worker_weights = np.log(sum_squared_errors/worker_errors)

			# Reshape weights 
			worker_weights = worker_weights.reshape(w_num,1)

			# Now have to calcualte the new truths 
			new_truths = (train_data.dot(worker_weights)/(np.sum(worker_weights))).reshape(E,1)

	return worker_weights

'''

data = np.array([[-1, -2,  0],
   [-1, -2,  0],
   [ 0, -2,  0],
   [ 0, -2,  0],
   [ 1, -2,  1],
   [ 1, -2,  1],
   [ 1, -2,  1],
   [ 1, -2,  1],
   [ 1, -2,  2],
   [ 1, -2,  2],
   [ 1, -2,  2],
   [ 1, -2,  2],
   [ 1, -2,  2],
   [ 1, -2,  2],
   [ 1, -2,  2],
   [ 1, -2,  2],
   [ 1, -2,  2],
   [ 1, -2,  2],
   [ 1, -2,  2],
   [ 1, -2,  2],
   [ 2, -2,  2],
   [ 2, -2,  2],
   [ 2,  1,  2],
   [ 2,  1,  2],
   [ 2,  1,  1],
   [ 2,  1,  1],
   [ 2,  1,  1],
   [ 2,  1,  1],
   [ 2,  1,  1],
   [ 2,  1,  2],
   [ 2,  1,  2],
   [ 2,  1,  2],
   [ 2,  1,  2],
   [ 3,  1,  3],
   [ 3,  1,  3],
   [ 3,  1,  3],
   [ 3,  1,  3],
   [ 4,  1,  2],
   [ 4,  1,  2],
   [ 4,  1,  2],
   [ 4,  1,  2],
   [ 4,  1,  3],
   [ 5,  1,  3],
   [ 5,  1,  3],
   [ 5,  5,  3],
   [ 5,  5,  3],
   [ 5,  5,  3],
   [ 5,  5,  3],
   [ 5,  5,  3],
   [ 6,  5,  3],
   [ 6,  5,  3],
   [ 6,  5,  3],
   [ 6,  5,  3],
   [ 6,  5,  3],
   [ 6,  5,  3],
   [ 6,  5,  3],
   [ 6,  5,  3],
   [ 6,  5,  3],
   [ 6,  5,  3],
   [ 6,  5,  3],
   [ 6,  5,  3],
   [ 6,  5,  4],
   [ 6,  5,  4],
   [ 6,  5,  4],
   [ 6,  5,  4],
   [ 5,  5,  4],
   [ 5,  6,  4],
   [ 6,  6,  4],
   [ 6,  6,  4],
   [ 7,  6,  4],
   [ 7,  6,  4],
   [ 8,  6,  5],
   [ 8,  6,  5],
   [ 8,  6,  5],
   [ 7,  6,  5],
   [ 7,  6,  5],
   [ 6,  6,  5],
   [ 6,  6,  5],
   [ 5,  6,  5],
   [ 5,  6,  5],
   [ 5,  6,  5],
   [ 5,  6,  5],
   [ 5,  6,  5],
   [ 5,  6,  5],
   [ 5,  6,  5],
   [ 5,  6,  5],
   [ 5,  6,  5],
   [ 5,  6,  5]])


weights_result = crh_init(data,3,88, 100)

print(weights_result)

'''


