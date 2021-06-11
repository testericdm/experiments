pragma solidity ^0.5.1;


// Worker Manager Contract, that keeps records of registered workers


contract Task {

// Currently only stores the reliabilities but can be used to store hashed certificates and etc for the workers
address owner;
mapping (address => uint256) public reliabilities;


constructor() public {
    owner = 0x0ea4ADdC16EcC58a72B0DAD9d381844A5E934D5E;
}



modifier IsCreator {
    require(msg.sender == owner, "Contract not called by creator");
    _;
}



function registerWorker(address  _name) public {
		reliabilities[_name] = 1;
		
	}

function UpdateWorker(address  _name, uint val) public {
		reliabilities[_name] = val;
		
	}
	
// Get Worker reliability

function getReliability(address _name) public view returns (uint256 ){
    return reliabilities[_name];
    
}
    
    
    
}


