const task = artifacts.require("./Task");
const td = artifacts.require("./TruthDiscovery");
const td2 = artifacts.require("./TruthDiscovery2");
const td3 = artifacts.require("./TruthDiscovery3");
const td4 = artifacts.require("./TruthDiscovery4");
const td5 = artifacts.require("./TruthDiscovery5");


var td_args = {ownerAddress : "0x0ea4ADdC16EcC58a72B0DAD9d381844A5E934D5E",
			   taskHash : "0x0ea4ADdC16EcC58a72B0DAD9d381844A5E934D5E",
			    requesterAdd : "0x0ea4ADdC16EcC58a72B0DAD9d381844A5E934D5E" ,
			      reputation : 50,
			      deadline : 150,
			   maxworkers : 50}


module.exports = function(deployer) {
  deployer.deploy(task);
  deployer.deploy(td, td_args.ownerAddress, td_args.taskHash, td_args.requesterAdd, td_args.reputation, td_args.deadline, td_args.maxworkers);
  deployer.deploy(td2, td_args.ownerAddress, td_args.taskHash, td_args.requesterAdd, td_args.reputation, td_args.deadline, td_args.maxworkers);
  deployer.deploy(td3, td_args.ownerAddress, td_args.taskHash, td_args.requesterAdd, td_args.reputation, td_args.deadline, td_args.maxworkers);
  deployer.deploy(td4, td_args.ownerAddress, td_args.taskHash, td_args.requesterAdd, td_args.reputation, td_args.deadline, td_args.maxworkers);
  deployer.deploy(td5, td_args.ownerAddress, td_args.taskHash, td_args.requesterAdd, td_args.reputation, td_args.deadline, td_args.maxworkers);
};
