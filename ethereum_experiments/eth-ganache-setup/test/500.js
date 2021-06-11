var Web3 = require('web3') ;

// const contract_json = require('./Task.json');
// const TD_contract_json = require('./TruthDiscovery.json');
var data_json = require('./new_data.json');
data_json = data_json[0];
// const contract_json = require('../build/contracts/Task.json');
// const TD_contract_json = require('../build/contracts/TruthDiscovery.json');
// const contract_json = require('./Task.json');
const contract_json = require('/Users/sid_mukkamala/Documents/Thesis2/code/truffleprojects/truffleanew/build/contracts/Task.json');
// const TD_contract_json = require('./TruthDiscovery.json');
const TD_contract_json = require('/Users/sid_mukkamala/Documents/Thesis2/code/truffleprojects/truffleanew/build/contracts/TruthDiscovery.json');
var vals = require('./keys.json');
var vals = vals[0];


// Connect to ganache, which is the web3 provider
var web3 = new Web3('http://127.0.0.1:8545') 
// var web3 = new Web3('http://host.docker.internal:8545') 

// Get the abi of the contract
var abi = contract_json.abi;

var TD_abi = TD_contract_json.abi;

// console.log(contract_json)

const publicKey = '0x0ea4ADdC16EcC58a72B0DAD9d381844A5E934D5E'
const privateKey = Buffer.from('0x8f89eabfb81dab20c40b96f5f52c5a4ac188994f59cbd9a966b9538f487ded0d', 'hex');



const user1 = "0x4c9A3691966A77907affA29d005F9dF2eA8ab656"; 
const user2 = "0x4b9bc05a3b2a4aeB2ce3868AfCaCD7C44Dc297dB";
const user3 = "0x5E68C86B731B33634878Fa3b5d2025EB113B3C8b"; 
const user4 = "0x138399fC1E777950f4630eeDf895c964aF83Cd85"; 
const user5 = "0xCF51E1a04934E9dfA7e891a9a38Af1CAdEbE35dd"; 


const privateKey1 = Buffer.from('0xd5952f33f220ae2975a0867e0b148109f34dfe5ab350622e8f37e6f7a5804456', 'hex');
const privateKey2 = Buffer.from('0xd822cf8318f5481012ea725e70895e8709a7f82d85dcbde3d7d058145936c2a1', 'hex');
const privateKey3 = Buffer.from('0xdf32528fe9309f22c1c1937e55ebfcfd13513c6b3cba357fc6e79a6531c488a1', 'hex');
const privateKey4 = Buffer.from('0x7658fd5e41605478d80c70a0097ec6aa0f3c27b33bd7759fa22d467bdd51eedb', 'hex');
const privateKey5 = Buffer.from('0x15ec0e458c8731a21ff5db62d24e01d3ba0e493e52a67d607f65a9be3784cca9', 'hex');




// Get the id and etc and store it
var id;
var deployed_network;
var TD_deployed_network;


var contract;
var TD_contract;

const set_up = async () => {

	// get the id of the session to get correct address of contract
	id = await web3.eth.net.getId();
	// Each time we migrate, it creates a new contract address, use session ID to get address 
	deployed_network = contract_json.networks[id];
	// Repeat for the TruthDiscovery contract
	TD_deployed_network = TD_contract_json.networks[id];

	// console.log(deployed_network, TD_deployed_network)


	// Create the contract with addresses and etc
	contract = new web3.eth.Contract(abi, deployed_network.address);
	TD_contract = new web3.eth.Contract(TD_abi, TD_deployed_network.address);

	console.log("Registring workers")
	
	// for (i = 0; i < 500; i++) {
	// 	TD_contract.methods.Add_worker(vals[i]).send({from: vals[i]});

	// }

	// for (i = 0; i < 500; i++) {
	// 		var curval = vals[i];
	// 		TD_contract.methods.UpdateHash(curval, curval).send({from: curval });

	// 	}

	// for (i = 0; i < 500; i++) {
	// 		var curval = vals[i];
	// 		TD_contract.methods.UpdateHash(curval, curval).send({from: curval });

	// 	}

	// for (i = 0; i < 500; i++) {
	// 		var curval = vals[i];
	// 		TD_contract.methods.UpdateHash(curval, curval).send({from: curval });

	// 	}

	for (i = 0; i < 10; i++) {
			var curval = vals[i];
			TD_contract.methods.UpdateHash(curval, curval).send({from: curval });

		}


		
	console.log("Registration Complete")




	


	// console.log(contract.methods)
	// await contract.methods.registerWorker("0x4c9A3691966A77907affA29d005F9dF2eA8ab656").send({
	// 	from: publicKey,
	// })
	// var reply = await contract.methods.getReliability("0x4c9A3691966A77907affA29d005F9dF2eA8ab656").call(); 
	// console.log(reply)


	// await contract.methods.UpdateWorker("0x4c9A3691966A77907affA29d005F9dF2eA8ab656", 321).send({
	// 	from: publicKey,
	// })

	// var reply = await contract.methods.getReliability("0x4c9A3691966A77907affA29d005F9dF2eA8ab656").call(); 
	// console.log(reply)

	// Here, do the following : Put a value in and then get the value out and see how they compare. Do it with multiple addresses and measure gas. 

	// await TD_contract.methods.Activate().call();

	// After activating, its over
	// data = data_json[epoch];

	// var pt_value = partial_truth(Workers,data)

	// await TD_contract.methods.sendData(pt_value[0]*100, pt_value[1]).send({
	// 	from:user1,
	// })

	// // Get the epoch value 
	// var value = await TD_contract.methods.getFinalTruth().call();
	// var value = value/100
	// console.log(value);

	// // Using final_truth, update the weights
	// worker_update(Workers,value);
	// console.log(Workers)

	// data = data_json[epoch];

	// var pt_value = partial_truth(Workers,data)

	// var partial_truth_scaled =  Math.round(pt_value[0]*10000)
	// var weights_scaled = Math.round(pt_value[1])
	// console.log("The submission values are: ", pt_value)
	// console.log("SCALED values are: ", partial_truth_scaled,weights_scaled)

	// await TD_contract.methods.sendData(partial_truth_scaled, weights_scaled).send({
	// 	from:user1,
	// })

	// var value = await TD_contract.methods.getFinalTruth().call()
	// console.log("INSIDE THE FUNC",value)

	// await TD_contract.methods.reset().send({from:user1})

	// var result = await TD_contract.methods.getVals().call()
	// console.log("Value should be zeros", result)


}


// const weightupdate = async () => {


// 	data = data_json[epoch];

// 	var pt_value = partial_truth(Workers,data)

// 	var partial_truth_scaled =  Math.round(pt_value[0]*10000)
// 	var weights_scaled = Math.round(pt_value[1])
// 	// console.log("The submission values are: ", pt_value)
// 	// console.log("SCALED values are: ", partial_truth_scaled,weights_scaled)

// 	await TD_contract.methods.sendData(partial_truth_scaled, weights_scaled).send({
// 		from:user1,
// 	})

	// if (epoch % 25 == 0) {
	// 	for (i = 0; i < 500; i++) {
	// 		var curval = vals[i];
	// 		TD_contract.methods.UpdateHash(curval, curval).send({from: curval });

	// 	}
	// }
// 	// var value = await TD_contract.methods.getFinalTruth().call()
// 	// console.log("INSIDE THE FUNC",value)

// 	// var result = await TD_contract.methods.getVals().call()
// 	// console.log("Value should be!", result)


// }

// const get_finaltruth = async () => {

// 	// Get the epoch value 
// 	var value = await TD_contract.methods.getFinalTruth().call();
// 	var value = value/10000
// 	console.log(value);

// 	// Using final_truth, update the weights
// 	worker_update(Workers,value);
// 	// console.log(Workers)

// 	epoch += 1;

// 	// await TD_contract.methods.reset().send({from:user1})

// 	if (epoch == 100) {
// 		clearInterval(Id);
// 	}
// }


// const resetvals = async () => {
// 	TD_contract.methods.reset().send({from:user1})
// }
// // THIS IS THE ONE

// // const weightupdate = async () => {


// // 	data = data_json[epoch];

// // 	var pt_value = partial_truth(Workers,data)

// // 	var partial_truth_scaled =  Math.round(pt_value[0]*100)
// // 	var weights_scaled = Math.round(pt_value[1])
// // 	console.log(partial_truth_scaled, weights_scaled)

// // 	await TD_contract.methods.sendData(partial_truth_scaled, weights_scaled).send({
// // 		from:user1,
// // 	})

// // 	// Get the epoch value 
// // 	var value = await TD_contract.methods.getFinalTruth().call();
// // 	var value = value/100
// // 	console.log(value);

// // 	// Using final_truth, update the weights
// // 	worker_update(Workers,value);
// // 	console.log(Workers)

// // 	epoch += 1;

// // 	if (epoch == 3) {
// // 		clearInterval(Id);
// // 	}
// // }





// // The client code - first iteration
// console.log("The first iteration of the client server")
// const libstat = require('jstat')
// // Import modules

// var FirstIter = false 
// const N = 100

// // Initialise the decay value
// const decay = 0.95
// const alpha = 0.05


// // HELPER FUNCTIONS START ===========

// function createWorker(idval) {
// 	return {
	
// 	id: idval,
// 	N : 1,
// 	Err: 1,
// 	weight :1,
// 	val: NaN
// 	}
// }

// function createWorkers(arr){
// 	var worker_lst = []

// 	arr.forEach(function (item){
// 		worker_lst.push(createWorker(item) )
// 	})

// 	return worker_lst
// }

// // HELPER FUNCTIONS END ===========


// // Create a function that takes a list of workers and data per epoch and calcualte partial truth.
// function partial_truth(workers_lst, data_lst){
// 	let pt = 0;
// 	let weights = 0;

// 	// Perform weighted averaging to get truth_value
// 	for (i = 0;i < N; i += 1) {
// 			workers_lst[i].val = data_lst[i]
// 		}

// 	// P.T. Calculation 
// 	// console.log(workers_lst)

// 	for (i = 0; i < N; i++) {
// 		temp_worker = workers_lst[i]
// 		pt += temp_worker.val * temp_worker.weight
// 		weights += temp_worker.weight

// 	}

// 	return [pt,weights]


// }

// // Create a function that updates the worker's weight after retriving the truth value computation 

// function worker_update(worker_lst, final_truth){
// // If the worker provided a value at this instance, then update the N count, after applying decay

// for (i = 0; i < N; i++) {
// 	temp_worker = worker_lst[i]


// 	worker_lst[i].N = 1 + temp_worker.N*decay
// 	worker_lst[i].Err = ((final_truth - temp_worker.val)**2) + temp_worker.Err*decay
// 	worker_lst[i].val = NaN

// }

	
// for (i = 0; i < N; i++) {
// 	// Carry out worker weight updates using confidence-aware (invese cdf function)
// 	worker_lst[i].weight = libstat.chisquare.inv( (1-alpha), worker_lst[i].N)/ worker_lst[i].Err
// }


// }

// function scehduler(){
//   setTimeout(weightupdate, 0);
//   setTimeout(get_finaltruth, 11000); 
//   setTimeout(resetvals,13000)

// } 



// // First Phase - Instantiating Workers with chosen IDs 

// var Workers = createWorkers([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]);
// // var pt = 0
// // var weights = 0
// var epoch = 0

// // SECOND PHASE - Data updates and partial truth computation

// // Assume the data is available as an array called data
// // where the index of the value corresponds to a worker submitting the data
// // var data = 0


set_up();
// // weightupdate();
// var Id = setInterval(scehduler, 15000);
// // weightupdate();



// // async function main() {

// // 	data = data_json

// // 	for (i = 0; i <100; i ++){
// // 		let counter = i;

// // 		let pt = await partial_truth(Workers,data[counter])
// // 		let value = pt[0]/pt[1]
// // 		await weightupdate(Workers, value)
// // 		console.log(pt)

// // 	}
	

// // }

// // main();













// if (FirstIter) {
// 	// For the very first round, we simply compute the mean of the values, instead of weighted averaging
// 	pt = data.reduce((a,b) => a + b, 0)/data.length
// 	FirstIter = false


// } else {

// 	// Perform weighted averaging to get truth_value
// 	for (i = 0;i < N; i += 1) {
// 		Workers[i].val = data[i]
// 	}



// // P.T. Calculation 

// 	for (i = 0; i < N; i++) {
// 		temp_worker = Workers[i]
// 		pt += temp_worker.val * temp_worker.weight
// 		weights += temp_worker.weight

// 	}	
// }

// console.log(pt, weights)








// // TODO: Create a way to read the values from (1.) a database or 
// //                                            (2.) as HTTP requested with data values 

// // We receive data as a key-value pair, where key is the IP address of worker and value is well, value

// // Write code that takes a key-value pair and updates the right worker's tempvalue. 

// // Here is where we retireve the final truth after sending it away.


// // Send partial truth value to the blockchain and retrieve full truth value,
// var final_truth = pt
// // Compute error and etc
// // Handle case with missing data 
// console.log(final_truth)


// // Do for all workers:
// // If the worker provided a value at this instance, then update the N count, after applying decay

// for (i = 0; i < N; i++) {
// 	temp_worker = Workers[i]
// 	if (isNaN(temp_worker.val)) {
// 		Workers[i].N = temp_worker.N*decay
// 		Workers[i].Err = temp_worker.Err*decay

// 	} else {

// 		Workers[i].N = 1 + temp_worker.N*decay
// 		Workers[i].Err = ((final_truth - temp_worker.val)**2) + temp_worker.Err*decay
// 		Workers[i].val = NaN

// 	}
// }

	
// for (i = 0; i < N; i++) {
// 	// Carry out worker weight updates using confidence-aware (invese cdf function)
// 	Workers[i].weight = libstat.chisquare.inv( (1-alpha), Workers[i].N)/ Workers[i].Err
// }


// // Carry out worker weight updates using confidence-aware (invese cdf function)
// // worker.weight = libstat.chisquare.inv( (1-alpha), worker.N)/ worker.Err


// // Save the worker weights to a distriubted storage like IPFS, including the values provided by the workers
// console.log(Workers)


// Checkpoints
// TODO: Compute Partial Truth 


// TODO: Using Partial Truth to compute new weights and error values


// TODO: Send Partial Truth to blockchain and retreive final truth. weights and error values


// TODO: Save worker data and new weights data in a database (IPFS is better)


// Template 

// 1. Initialize all workers and their values and etc
// 2. Wrap the worker weight adjustments and recomputation of weights etc in a function called workerUpdate. 
// 3. Take the first batch of values and push them into blockchain/
// 4. Use that async function to call the worker update function after retrieving the final value.
// 5. Wrap the main function that handles this in a setInterval to keep updating the values. Find a way to update data_values.









