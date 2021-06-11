import numpy as np 
import json

def normal_data(workers, epochs):
	# Draw a worker's reliability from a uniform distribution
	
	reliability = np.random.uniform(0,3,workers)
	# reliability = np.random.gamma(1,2,workers)
	# reliability = np.random.beta(0.5,0.5,workers)
	lst = creating_data_from_reliability(epochs, reliability)

	data = np.concatenate(lst, axis = 1)

	return data, reliability

def creating_data_from_reliability(epochs, reliability):
	# Created streaming data as epochs data, use normal distrubtion to create a worker's data
	lst = []
	for worker in reliability:
		lst.append(np.random.normal(0,worker,epochs).reshape(epochs, 1))
	return lst

def hash_values(arr):
	decimalised_vals = np.around(arr, 3).tolist()
	new_lst=[str(val) for val in decimalised_vals]

	str_val = "".join(new_lst)

	return hash(str_val)




data, reliability = normal_data(1000,100)

# data_lst1 = np.around(data[:,:50])

data_lst = np.around(data).tolist()
to_json_data = {"0":data_lst}

with open('../truffleprojects/truffleFinal/test/data_1000.json', 'w') as f:
	json.dump(to_json_data, f)
# print(data)
# print()

# To get the first column of the matrix, use data[:,0] , this will correspond to a worker's data through the whole process
# Round to three decimal places and then append as string, then hash

# data_lst1 = np.around(data[:,:33],2).tolist()
# data_lst2 = np.around(data[:,33:66],2).tolist()
# data_lst3 = np.around(data[:,66:],2).tolist()
# to_json1 = {"0":data_lst1}
# to_json2 = {"0":data_lst2}
# to_json3 = {"0":data_lst3}


# with open('../truffleprojects/truffleFinal/test/data_client2_1.json', 'w') as f:
# 	json.dump(to_json1, f)

# with open('../truffleprojects/truffleFinal/test/data_client2_2.json', 'w') as f:
# 	json.dump(to_json2, f)

# with open('../truffleprojects/truffleFinal/test/data_client2_3.json', 'w') as f:
# 	json.dump(to_json3, f)
# # print(data[:,:50].shape)
# print(data[:,50:].shape)




