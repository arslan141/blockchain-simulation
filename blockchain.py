import hashlib
import time
from datetime import datetime

# Define the structure of a Block
class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = datetime.utcnow().isoformat()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return self.hash_block(self.index, self.timestamp, self.transactions, self.previous_hash)

    @staticmethod
    def hash_block(index, timestamp, transactions, previous_hash):
        block_string = f"{index}{timestamp}{transactions}{previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

# Define the Blockchain class
class Blockchain:
    def __init__(self, chain=None):
        if chain:
            self.chain = chain
        else:
            self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # The first block in the chain
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), transactions, previous_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                print(f"Validation failed: Block {current_block.index} hash mismatch.")
                return False

            # Check if the current block's previous hash matches the previous block's hash
            if current_block.previous_hash != previous_block.hash:
                print(f"Validation failed: Block {current_block.index} previous hash mismatch.")
                return False

        return True

# Demonstrate
if __name__ == "__main__":
    # Create the blockchain
    my_blockchain = Blockchain()

    # Add blocks with dummy transactions
    my_blockchain.add_block("Transaction 1: arslan pays sid 10 BTC")
    my_blockchain.add_block("Transaction 2: sid pays quad 5 BTC")

    # Print the blockchain
    for block in my_blockchain.chain:
        print(f"Block {block.index}:")
        print(f"  Timestamp: {block.timestamp}")
        print(f"  Transactions: {block.transactions}")
        print(f"  Previous Hash: {block.previous_hash}")
        print(f"  Hash: {block.hash}\n")

    # Validate the blockchain
    print("Is blockchain valid?", my_blockchain.is_chain_valid())
