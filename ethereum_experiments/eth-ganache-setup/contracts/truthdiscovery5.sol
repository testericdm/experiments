pragma solidity ^0.5.1;

contract TruthDiscovery5 { 
    
    address owner;
    
    address requester;
    bytes task;
    
    uint epoch_num = 0;
    
    int sum_weights = 0;
    int sum_numerator = 0;

    int finaltruth = 0;
    
    // Requires store minimum reputation value required and etc 
    
    uint min_reputation;
    uint time_deadline;
    
    uint num_workers_registered = 0;

    mapping (address => address) public hashes;
    
    uint max_workers;
    
    address[]  workers;
    // Use this to perform TruthDiscovery and measure gas consumption
    
    // Have multiple states to figure out what actions are allowed and which arent 
    
    enum ContractState{Init, InEpoch, EndEpoch, Terminated}
    
    // Set first initial state to Init
    ContractState contract_state = ContractState.Init;
    
    
    
    // Modifiers to make code readable 
    // Modifier that checks if we are in init state
    modifier InInitState() {
        require(contract_state == ContractState.Init, "Contract not in the Init State");
        _;
    }
    
    modifier CanBeActivated() {
        require(contract_state == ContractState.Init || contract_state == ContractState.EndEpoch );
        _;
    }
    
    // Create constructor with task details 
    
    constructor(address owner_crwd, bytes memory task_hash ,address requester_add, uint reputation, uint deadline, uint maxworkers) public {
        
        owner = owner_crwd;
        task = task_hash;
        requester = requester_add;
        min_reputation = reputation;
        time_deadline = deadline;
        max_workers = maxworkers;
        workers = new address[](maxworkers);
        
    }
    
    modifier IsCreator {
    require(msg.sender == owner, "Contract not called by creator");
    _;
}
    
    // A function that adds workers to this task, can only be performed in the init state
    function Add_worker(address add) InInitState public {
        require(msg.sender == add, "Only a worker can register themselves");
        workers[num_workers_registered] = add;
    }

    function UpdateHash(address  _name, address val) public {
        hashes[_name] = val;
        
    }
    
    // Need a function that changes state to begin Epoch
    function Activate() IsCreator CanBeActivated public {
        sum_numerator = 0;
        sum_weights = 0;
        contract_state = ContractState.InEpoch;
        epoch_num = epoch_num + 1;
    } 
    
    // Ends an epoch 
    function EndEpoch() IsCreator public {
        contract_state = ContractState.EndEpoch;
    }
    
    // Do the actual truth Disocvery during epoch time, simply add up the weights + weighted values 
    function sendData(int val, int weight ) public {
        sum_numerator += val;
        sum_weights += weight;

        // if (num_participants_counter == 5) {
        //     if (sum_weights == 0) {
        //         finaltruth = 0;
        //     }
        //     else {
        //     finaltruth = sum_numerator/sum_weights; 
        //     }
            
        //     sum_numerator = 0;
        //     sum_weights = 0;
        //     num_participants_counter = 0;
        // }
    }
    
    // Once an epoch has ended have a way of getting the final truth
    // function getFinalTruth() public view returns (int ){
    function getFinalTruth() public view returns (int){

         if (sum_weights == 0){
            return 0;
        }
        else {
            return sum_numerator/sum_weights;
        }
        // int temp = sum_numerator/sum_weights; 
        // sum_weights = 0;
        // sum_numerator = 0;
        // return temp;
        // }
        // return finaltruth;
        // if (sum_weights == 0){
        //     return 0;
        // }
        // else {
        //     finaltruth = sum_numerator/sum_weights; 
        //     sum_weights = 0;
        //     sum_numerator = 0;
        //     return finaltruth;
        // }
}

    function getEpochNum() public view returns (uint) {
        return epoch_num;
    }

    function reset() public {
        sum_weights = 0;
        sum_numerator = 0;

    }

    function getVals() public view returns (int,int){
        return (sum_numerator, sum_weights);
    }
    
    function Terminate() IsCreator public {
        contract_state = ContractState.Terminated;
    }
    
    
}