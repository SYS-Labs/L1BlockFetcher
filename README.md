# L1-L2 Block Correspondence Script

This Python script allows you to find the corresponding L1 block for a given L2 block on the Rollux network. It leverages Web3.py to interact with the Ethereum node and the `L1Block` contract deployed on the L2 network.

## Prerequisites

Before running the script, ensure you have Python 3.7 or higher installed.

The script depends on the packages listed in `requirements.txt`. To install the required packages, run:

```bash
pip install -r requirements.txt
```

## Usage
### Clone the Repository

```bash
git clone https://github.com/your-username/l1-l2-block-correspondence.git
cd L1BlockFetcher
```

## Running the script
```bash
python main.py --l2_block_number <L2_BLOCK_NUMBER> [--rpc_url <RPC_URL>] [--l1block_contract <L1BLOCK_CONTRACT_ADDRESS>]
```

### Parameters

- --l2_block_number (required): The L2 block number you want to query.
- --rpc_url (optional): The RPC URL for the Rollux node. Defaults to https://rpc.rollux.com.
- --l1block_contract (optional): The address of the L1Block contract. Defaults to 0x4200000000000000000000000000000000000015.

### Example
To find the corresponding L1 block for L2 block number 5000, run:
```bash
python main.py --l2_block_number 5000
```
You can also specify a custom RPC URL and L1Block contract address:
```bash
python main.py --l2_block_number 5000 --rpc_url "https://custom-rpc-url.com" --l1block_contract "0xYourContractAddress"
```

### Output
- The corresponding L1 block number for the specified L2 block.
- The timestamp of the L1 block.
- The sequence number of L2 blocks within the current epoch.