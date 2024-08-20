from web3 import Web3
import argparse

# Function to get the corresponding L1 block for an L2 block
def get_l1_block_for_l2_block(l2_block_number, rpc_url, l1block_contract):
    web3 = Web3(Web3.HTTPProvider(rpc_url))

    # Check connection
    if not web3.is_connected():
        raise Exception("Failed to connect to Rollux node")

    l1_block_contract_address = Web3.to_checksum_address(l1block_contract)

    # ABI for the L1Block contract (only the necessary parts)
    l1_block_abi = [
        {
            "constant": True,
            "inputs": [],
            "name": "number",
            "outputs": [{"name": "", "type": "uint64"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [],
            "name": "sequenceNumber",
            "outputs": [{"name": "", "type": "uint64"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [],
            "name": "timestamp",
            "outputs": [{"name": "", "type": "uint64"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
    ]

    l1_block_contract = web3.eth.contract(address=l1_block_contract_address, abi=l1_block_abi)

    # Get the current L1 block data from the L1Block contract
    l1_block_number = l1_block_contract.functions.number().call()
    l1_sequence_number = l1_block_contract.functions.sequenceNumber().call()
    l1_timestamp = l1_block_contract.functions.timestamp().call()

    # Fetch the L2 block timestamp (requires connection to L2 node)
    l2_block = web3.eth.get_block(l2_block_number)
    l2_timestamp = l2_block['timestamp']

    # Compare the L2 block timestamp with the known L1 block timestamp
    if l2_timestamp >= l1_timestamp:
        print(f"L2 Block {l2_block_number} (Timestamp: {l2_timestamp}) likely corresponds to L1 Block {l1_block_number} (Timestamp: {l1_timestamp})")
    else:
        print("L2 Block's timestamp predates the current epoch; it might belong to a previous L1 block.")
        l1_block_number = None
        # Additional logic could be added here to track back to the correct L1 block if needed.

    print(f"L1 Block Number: {l1_block_number}")
    print(f"L1 Timestamp: {l1_timestamp}")
    print(f"L2 Timestamp: {l2_timestamp}")
    print(f"L2 Sequence Number: {l1_sequence_number}")

if __name__ == "__main__":
    # Setup CLI argument parser
    parser = argparse.ArgumentParser(description="Get the corresponding L1 block for a given L2 block.")
    parser.add_argument("--l2_block_number", type=int, required=True, help="L2 block number to query")
    parser.add_argument("--rpc_url", type=str, default="https://rpc.rollux.com", help="RPC URL for the Rollux node")
    parser.add_argument("--l1block_contract", type=str, default="0x4200000000000000000000000000000000000015", help="Address of the L1Block contract")

    # Parse the arguments
    args = parser.parse_args()

    # Get the L1 block for the specified L2 block number
    get_l1_block_for_l2_block(args.l2_block_number, args.rpc_url, args.l1block_contract)
