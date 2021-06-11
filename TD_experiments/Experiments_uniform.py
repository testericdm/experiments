# Here I will create simulated data

import numpy as np 
import dynaTD
import catd
import streaming_catd
import TruthFinder as tf
import crh 

# Helper Functions
def RMSE(arr):
	return np.sqrt(np.sum(arr ** 2)/len(arr))

def MAE(arr):
	return np.sum(np.abs(arr))/len(arr)

# Function that creates a normal dist dataset with uniform worker weights

def normal_data(workers, epochs):
	# Draw a worker's reliability from a uniform distribution
	
	reliability = np.random.uniform(0,3,workers)
	#reliability = np.random.gamma(1,2,workers)
	#reliability = np.random.beta(0.5,0.5,workers)

	# Created streaming data as epochs data, use normal distrubtion to create a worker's data
	# lst = []
	# counter = 0
	# for worker in reliability:
	# 	lst.append(np.random.normal(0,worker,epochs).reshape(epochs, 1))
	# 	if counter == 0:
	# 		print("here")
	# 	counter += 1

	lst = creating_data_from_reliability(epochs, reliability)

	data = np.concatenate(lst, axis = 1)

	return data, reliability

def creating_data_from_reliability(epochs, reliability):
	# Created streaming data as epochs data, use normal distrubtion to create a worker's data
	lst = []
	for worker in reliability:
		lst.append(np.random.normal(0,worker,epochs).reshape(epochs, 1))
	return lst

def transition_data(workers, epochs,old_reliability, total_increments = 10):


	new_reliability = np.random.uniform(0,3,workers)

	transition_data_lst = []

	for i in range(workers):
		old_real = old_reliability[i]
		new_real = new_reliability[i]

		dist_vals = np.linspace(old_real, new_real, num = total_increments)

		# To store new SDs
		temp_lst = []

		# We get small increments of 10 or whatever value is chosen
		# For each increment, get a data point by pulling from normal distribution
		for SD_val in dist_vals:
			temp_lst.append(np.random.normal(0,SD_val))

		# Once all transition data for each worker has been computed, store it in a list to later be matrix 
		# TODO: Standardize by putting in a parameter instead of actual vals (replace 10 to # increments)

		transition_data_lst.append(np.array(temp_lst).reshape(total_increments,1))

	# Convert transition list into transition matrix

	trans_data = np.concatenate(transition_data_lst, axis = 1)

	return trans_data, new_reliability



# # Running Experiment with constant reliability 

# print("Initial Constant Reliability:")
# data, init_reliabilily_vals = normal_data(100,100)

# # Mean Results
# mean_vals = np.mean(data, axis = 1)
# # print("SHape of Mean vals is: ", mean_vals.shape)

# # Running DynaTD
# results_dyna = dynaTD.dyna_TD(data,100,100)

# # CATD Results
# catd_weights = catd.catd_init(data, 100, 100)
# results_catd = data.dot(catd_weights)/(np.sum(catd_weights))

# results_catd_stream = streaming_catd.streaming_catd_init(data, 100, 100)
# print("Mean is: ", RMSE(mean_vals),"CATD: ", RMSE(results_catd), " DynaTD: ", RMSE(results_dyna), " CATD_D: ", RMSE(results_catd_stream))

# print(" ")
# print("=========== END ===========")

# # RUNNING EXPERIMENTS WITH VARIABLE RELIABILITY

# print("Variable Reliability:")

# trans_data, new_reliability_vals = transition_data(100,100,init_reliabilily_vals)

# # Get epochs data with new reliability values
# new_data = np.concatenate(creating_data_from_reliability(100,new_reliability_vals), axis = 1) 

# # print(trans_data.shape,"and the rest is: ", new_data.shape)
# data = np.vstack((trans_data, new_data))
# # print(data.shape)
# # Mean Results
# mean_vals = np.mean(data, axis = 1)
# # print("SHape of Mean vals is: ", mean_vals.shape)

# # Running DynaTD
# results_dyna = dynaTD.dyna_TD(data,100,110)

# # CATD Results
# # catd_weights = catd.catd_init(data, 100, 110)
# results_catd = data.dot(catd_weights)/(np.sum(catd_weights))

# results_catd_stream = streaming_catd.streaming_catd_init(data, 100, 110)
# print("Mean is: ", RMSE(mean_vals),"CATD: ", RMSE(results_catd), " DynaTD: ", RMSE(results_dyna), " CATD_D: ", RMSE(results_catd_stream))



# Find a way to run the experiments multiple times 

# Save experiments in a dictionary 
num_experiments = 100
results_dict = {}

results_dict2 = {}

# Initialize all values to 0
results_dict["mean"] = 0
results_dict["median"] = 0
results_dict["truthfinder"] = 0
results_dict["dynatd"] = 0
results_dict["dynatd_smoothing"] = 0
results_dict["dynatd_decay"] = 0
results_dict["dynatd_ALL"] = 0

results_dict["catd"] = 0
results_dict["streaming_catd"] = 0
results_dict["crh"] = 0



results_dict2["mean"] = 0
results_dict2["median"] = 0
results_dict2["truthfinder"] = 0
results_dict2["dynatd"] = 0
results_dict2["dynatd_smoothing"] = 0
results_dict2["dynatd_decay"] = 0
results_dict2["dynatd_ALL"] = 0

results_dict2["catd"] = 0
results_dict2["streaming_catd"] = 0
results_dict2["crh"] = 0

for i in range(num_experiments):
	# Running Experiment with constant reliability 
	print("Running experiment number: ", i)
	# print("Initial Constant Reliability:")
	data, init_reliabilily_vals = normal_data(100,100)

	# Mean Results
	mean_vals = np.mean(data, axis = 1)

	# Running DynaTD
	results_dyna, results_dyna_smoothing, results_dyna_decay,results_dyna_ALL  = dynaTD.dyna_TD(data,100,100)

	# CATD Results
	catd_weights = catd.catd_init(data, 100, 100)
	results_catd = data.dot(catd_weights)/(np.sum(catd_weights))

	results_catd_stream = streaming_catd.streaming_catd_init(data, 100, 100)
	# print("Mean is: ", RMSE(mean_vals),"CATD: ", RMSE(results_catd), " DynaTD: ", RMSE(results_dyna), " CATD_D: ", RMSE(results_catd_stream))

	# TruthFinder Results
	tf_weights = tf.Truth_Finder(data, 100, 100)
	results_tf = data.dot(tf_weights)/(np.sum(tf_weights))

	# CRH results
	crh_weights = crh.crh_init(data,100,100, 20)

	# print(" ")
	# print("=========== END ===========")

	# RUNNING EXPERIMENTS WITH VARIABLE RELIABILITY

	# print("Variable Reliability:")

	trans_data, new_reliability_vals = transition_data(100,100,init_reliabilily_vals)

	# Get epochs data with new reliability values
	new_data = np.concatenate(creating_data_from_reliability(100,new_reliability_vals), axis = 1) 

	# print(trans_data.shape,"and the rest is: ", new_data.shape)
	data = np.vstack((trans_data, new_data))
	# print(data.shape)
	# Mean Results
	mean_vals = np.mean(data, axis = 1)

	# Median Results
	median_vals = np.median(data, axis = 1)

	# Running DynaTD
	results_dyna,results_dyna_smoothing, results_dyna_decay,results_dyna_ALL = dynaTD.dyna_TD(data,100,110)

	# CATD Results
	# catd_weights = catd.catd_init(data, 100, 110)
	results_catd = data.dot(catd_weights)/(np.sum(catd_weights))

	results_tf = data.dot(tf_weights)/(np.sum(tf_weights))

	results_crh = data.dot(crh_weights)/(np.sum(crh_weights))

	results_catd_stream = streaming_catd.streaming_catd_init(data, 100, 110)
	# print("Mean is: ", RMSE(mean_vals),"Median is: ", RMSE(median_vals) ,"CATD: ", RMSE(results_catd), " DynaTD: ", RMSE(results_dyna), " CATD_D: ", RMSE(results_catd_stream))
	# results_dict["mean"] += RMSE(mean_vals)
	# results_dict["median"] += RMSE(median_vals)
	# results_dict["truthfinder"] += RMSE(results_tf)
	# results_dict["dynatd"] += RMSE(results_dyna)
	# results_dict["dynatd_smoothing"] += RMSE(results_dyna_smoothing)
	# results_dict["dynatd_decay"] += RMSE(results_dyna_decay)
	# results_dict["dynatd_ALL"] += RMSE(results_dyna_ALL)
	# results_dict["catd"] += RMSE(results_catd)
	# results_dict["streaming_catd"] += RMSE(results_catd_stream)

	results_dict["mean"] += MAE(mean_vals)
	results_dict["median"] += MAE(median_vals)
	results_dict["truthfinder"] += MAE(results_tf)
	results_dict["dynatd"] += MAE(results_dyna)
	results_dict["dynatd_smoothing"] += MAE(results_dyna_smoothing)
	results_dict["dynatd_decay"] += MAE(results_dyna_decay)
	results_dict["dynatd_ALL"] += MAE(results_dyna_ALL)
	results_dict["catd"] += MAE(results_catd)
	results_dict["streaming_catd"] += MAE(results_catd_stream)
	results_dict["crh"] += MAE(results_crh)

	results_dict2["mean"] += RMSE(mean_vals)
	results_dict2["median"] += RMSE(median_vals)
	results_dict2["truthfinder"] += RMSE(results_tf)
	results_dict2["dynatd"] += RMSE(results_dyna)
	results_dict2["dynatd_smoothing"] += RMSE(results_dyna_smoothing)
	results_dict2["dynatd_decay"] += RMSE(results_dyna_decay)
	results_dict2["dynatd_ALL"] += RMSE(results_dyna_ALL)
	results_dict2["catd"] += RMSE(results_catd)
	results_dict2["streaming_catd"] += RMSE(results_catd_stream)
	results_dict2["crh"] += RMSE(results_crh)

for key,val in results_dict.items():
	print(key, " MAE value is: ",val/num_experiments)


for key,val in results_dict2.items():
	print(key, " rMSE value is: ",val/num_experiments)










