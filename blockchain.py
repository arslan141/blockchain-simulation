import hashlib
from argon2 import PasswordHasher
from datetime import datetime

# Define the structure of a Block
class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = None  # Finalized after proof-of-work

    def calculate_proof_hash(self):
        """
        Use SHA-256 for proof-of-work hash calculation.
        """
        block_data = (
            str(self.index) +
            str(self.transactions) +
            str(self.timestamp) +
            str(self.previous_hash) +
            str(self.nonce)
        )
        return hashlib.sha256(block_data.encode()).hexdigest()

    def finalize_hash(self):
        """
        Use Argon2 to calculate the final secure hash after proof-of-work.
        """
        ph = PasswordHasher()
        block_data = (
            str(self.index) +
            str(self.transactions) +
            str(self.timestamp) +
            str(self.previous_hash) +
            str(self.nonce)
        )
        try:
            return ph.hash(block_data)
        except Exception as e:
            return None

# Define the Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # Number of leading zeros required in the hash for proof-of-work

    def create_genesis_block(self):
        # The first block in the chain
        return Block(0, "Genesis Block", self.get_current_time(), "0")

    def get_current_time(self):
        # Get the current time in a human-readable format
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        # Create a new block and add it to the chain
        new_block = Block(
            index=len(self.chain),
            transactions=transactions,
            timestamp=self.get_current_time(),
            previous_hash=self.get_latest_block().hash
        )
        self.proof_of_work(new_block)
        new_block.hash = new_block.finalize_hash()
        self.chain.append(new_block)

    def proof_of_work(self, block):
        """
        Perform proof-of-work by finding a hash with a specific number of leading zeros.
        """
        while True:
            block.nonce += 1
            proof_hash = block.calculate_proof_hash()
            if proof_hash.startswith("0" * self.difficulty):
                break

    def is_chain_valid(self):
        # Validate the blockchain
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate the proof-of-work hash
            if not current_block.calculate_proof_hash().startswith("0" * self.difficulty):
                print(f"Validation failed: Block {current_block.index} proof-of-work mismatch.")
                return False

            # Validate the final hash
            if current_block.hash != current_block.finalize_hash():
                print(f"Validation failed: Block {current_block.index} hash mismatch.")
                return False

            if current_block.previous_hash != previous_block.hash:
                print(f"Validation failed: Block {current_block.index} previous hash mismatch.")
                return False

        return True

# Demonstrate
if __name__ == "__main__":
    # Create the blockchain
    my_blockchain = Blockchain()

    # Add blocks with dummy transactions
    my_blockchain.add_block(["Transaction 1: Arslan pays Sid 10 BTC"])
    my_blockchain.add_block(["Transaction 2: Sid pays Quad 5 BTC"])

    # Print the blockchain
    for block in my_blockchain.chain:
        print(f"Block {block.index}:")
        print(f"  Timestamp: {block.timestamp}")
        print(f"  Transactions: {block.transactions}")
        print(f"  Previous Hash: {block.previous_hash}")
        print(f"  Hash: {block.hash}")
        print(f"  Nonce: {block.nonce}\n")

    # Validate the blockchain
    print("Is blockchain valid?", my_blockchain.is_chain_valid())
