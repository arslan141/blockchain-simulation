# blockchain-simulation
 Blockchain Simulation
This project is a basic implementation of a blockchain simulation in Python. It demonstrates the core concepts of blockchain, including linked blocks, hashing, and chain validation.
Features
	• Each block contains: 
		○ Index
		○ Timestamp (ISO 8601 format)
		○ List of transactions
		○ Hash of the previous block
		○ Current block hash
	• Uses Argon2 for hashing.
	• Detects tampering by validating the blockchain.
	• Genesis block creation.
Prerequisites
	• Python 3.6 or above.
Setup Instructions
	1. Clone the repository or download the code files.
	2. Ensure Python is installed on your machine.
	3. Install any required dependencies (if necessary). This code uses Python's built-in libraries, so no additional installations are typically needed.
How to Run
	1. Open a terminal or command prompt.
	2. Navigate to the directory containing the code file.
	3. Run the following command: 
python simple_blockchain.py
	4. The program will: 
		○ Add example transactions to the blockchain.
		○ Print each block's details.
		○ Validate the blockchain and output the result.

Code Structure
	• Block Class: Defines the structure and hashing logic for each block.
	• Blockchain Class: Manages the chain and includes methods to add blocks and validate the chain.
Future Enhancements
	• Implement Proof-of-Work.
	• Add a feature to dynamically add transaction 

