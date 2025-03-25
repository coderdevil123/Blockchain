# Blockchain
Overview

This is a simple blockchain simulation built using Python. It demonstrates the core functionalities of a blockchain, including block creation, hashing, proof-of-work, and integrity validation.

Features

Block structure with transactions, timestamps, and cryptographic hashes

Proof-of-Work mechanism for block mining

Blockchain integrity validation

Demonstration of blockchain tampering detection

Installation

Prerequisites

Ensure you have Python installed (Python 3.x recommended).

Steps

Clone the repository:

git clone https://github.com/your-username/basic-blockchain-simulation.git
cd basic-blockchain-simulation

Run the blockchain simulation:

python blockchain.py

Usage

This script simulates:

Adding blocks with transactions.

Printing the blockchain.

Validating the blockchain before and after tampering.

Example Output

Block 0: Hash=<GENESIS_HASH>, PrevHash=0, Transactions=['Genesis Block']
Block 1: Hash=<BLOCK_HASH>, PrevHash=<GENESIS_HASH>, Transactions=['Alice pays Bob 10 BTC', 'Bob pays Charlie 5 BTC']
Block 2: Hash=<BLOCK_HASH>, PrevHash=<BLOCK_HASH>, Transactions=['Charlie pays Dave 2 BTC']

Blockchain valid? True

# Tampering with a transaction
Blockchain valid after tampering? False

Demonstration of Tampering Detection

To showcase how blockchain prevents unauthorized changes, the script modifies a transaction in an existing block and checks if the blockchain remains valid.

Contributing

Feel free to fork this repository, add improvements, and create a pull request.

License

MIT License

