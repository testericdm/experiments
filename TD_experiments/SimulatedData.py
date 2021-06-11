# Here I will create simulated data

import numpy as np 
import dynaTD
import catd
import streaming_catd
import TruthFinder as tf

# Helper Functions
def RMSE(arr):
	return np.sqrt(np.sum(arr ** 2)/len(arr))


# Number of workers in the experiment 
workers = 100
epochs = 100
# Draw a worker's reliability from a uniform distribution 
reliability = np.random.uniform(0,3,workers)

# Created streaming data as epochs data, use normal distrubtion to create a worker's data
lst = []
counter = 0
for worker in reliability:
	lst.append(np.random.normal(0,worker,epochs).reshape(epochs, 1))
	if counter == 0:
		print("here")
	counter += 1

data = np.concatenate(lst, axis = 1)

# print(data)

# The place where we test all the things
# data.dump("data_matrix.dat")

# DynaTD

results_dyna = dynaTD.dyna_TD(data,100,100)


# Mean Results
mean_vals = np.mean(data, axis = 1)

# CATD Results
catd_weights = catd.catd_init(data, 100, 100)
results_catd = data.dot(catd_weights)/(np.sum(catd_weights))

# print("For CATD, the values are: ",RMSE(results),"Where as, the mean error is: ", RMSE(mean_vals) )
print("Mean is: ", RMSE(mean_vals),"CATD: ", RMSE(results_catd), " DynaTD: ", RMSE(results_dyna))

tf_weights = tf.Truth_Finder(data, 100, 100)
results_tf = data.dot(tf_weights)/(np.sum(tf_weights))
print("The TF weights are : ", RMSE(results_tf))
# print("ANSWER IS : ", catd_weights)

# Proper experimentation values here ===== UNCOMMENT TO FOLLOW ==========

# # Streaming CATD results

# results = streaming_catd.streaming_catd_init(data, 100, 100)

# print("For streaming version they are: ", RMSE(results))



# # The next part is to resample the distrubtions

# # TODO :
# # Resample a 100 new reliability values, call them new_reliability

# # First get all the original reliability values, 
# # make 100 increments to go from original reliability to new reliability and use these values to create a data set by sampling with these new SDs:


# # Use workers to iterate 
# new_reliability = np.random.uniform(0,3,workers)

# transition_data_lst = []

# for i in range(workers):
# 	old_real = reliability[i]
# 	new_real = new_reliability[i]

# 	dist_vals = np.linspace(old_real, new_real, num = 10)

# 	# To store new SDs
# 	temp_lst = []

# 	# We get small increments of 10 or whatever value is chosen
# 	# For each increment, get a data point by pulling from normal distribution
# 	for SD_val in dist_vals:
# 		temp_lst.append(np.random.normal(0,SD_val))

# 	# Once all transition data for each worker has been computed, store it in a list to later be matrix 
# 	# TODO: Standardize by putting in a parameter instead of actual vals (replace 10 to # increments)

# 	transition_data_lst.append(np.array(temp_lst).reshape(10,1))

# # Convert transition list into transition matrix

# trans_data = np.concatenate(transition_data_lst, axis = 1)


# # Now we have the data matrix

# # We now create another matrix with new reliabilily metrics and lets see how it performs!
# lst = []
# counter = 0
# for worker in new_reliability:
# 	lst.append(np.random.normal(0,worker,epochs).reshape(epochs, 1))
# 	if counter == 0:
# 		print("here")
# 	counter += 1

# # Contains data sampled from new distribution 
# new_data = np.concatenate(lst, axis = 1)



# # Combine trans data with new_data

# test_data = np.vstack((trans_data, new_data))




# # Basically test whether CATD-D performs better than CATD when reliabililty changes

# answers = np.mean(test_data, axis = 1)


# # CATD values

# results_catd = test_data.dot(catd_weights)/(np.sum(catd_weights))

# # For the test of streaming catd, train on the whole data set

# streaming_catd_data = np.vstack((data,test_data))

# results_catd_stream = streaming_catd.streaming_catd_init(streaming_catd_data, 100, 210, decay = 0.95)

# # Print Results

# print("For CATD, the values are: ",RMSE(results_catd),"Where as, the mean error is: ", RMSE(answers) )
# print("For streaming version they are: ", RMSE(results_catd_stream))




