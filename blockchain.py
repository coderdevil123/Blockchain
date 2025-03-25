import hashlib
import time
import json

class Block:
    def __init__(self, index, transactions, previous_hash, nonce=0):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_data = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_data.encode()).hexdigest()

class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()
    
    def create_genesis_block(self):
        genesis_block = Block(0, ["Genesis Block"], "0")
        self.chain.append(genesis_block)
    
    def add_block(self, transactions):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), transactions, previous_block.hash)
        self.proof_of_work(new_block)
        self.chain.append(new_block)
    
    def proof_of_work(self, block):
        while not block.hash.startswith("0" * self.difficulty):
            block.nonce += 1
            block.hash = block.compute_hash()
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            
            if current.hash != current.compute_hash():
                return False
            
            if current.previous_hash != previous.hash:
                return False
        
        return True

    def print_chain(self):
        for block in self.chain:
            print(f"Block {block.index}: Hash={block.hash}, PrevHash={block.previous_hash}, Transactions={block.transactions}\n")

# Simulating the blockchain
blockchain = Blockchain()
blockchain.add_block(["Alice pays Bob 10 BTC", "Bob pays Charlie 5 BTC"])
blockchain.add_block(["Charlie pays Dave 2 BTC"])
blockchain.print_chain()

print("Blockchain valid?", blockchain.is_chain_valid())

# Tampering with the blockchain
blockchain.chain[1].transactions = ["Alice pays Bob 100 BTC"]  # Modifying transaction
print("Blockchain valid after tampering?", blockchain.is_chain_valid())
