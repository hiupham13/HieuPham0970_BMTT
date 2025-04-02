from blockchain import Blockchain

my_blockchain = Blockchain()

my_blockchain.add_transaction(sender="Alice", receiver="Bob", amount=50)
my_blockchain.add_transaction(sender="Bob", receiver="Charlie", amount=30)
my_blockchain.add_transaction(sender="Charlie", receiver="Alice", amount=20)

previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash
my_blockchain.add_transaction(sender="Genesis", receiver="Miner", amount=50)
new_block = my_blockchain.create_block(new_proof, previous_hash)

for block in my_blockchain.chain:
    print(f"Block {block.index}:\n"
          f"Hash: {block.hash}\n"
          f"Previous Hash: {block.previous_hash}\n"
          f"Timestamp: {block.timestamp}\n"
          f"Transactions: {block.transactions}\n"
          f"Proof: {block.proof}\n"
          "--------------------------------------------------") 
print("Blockchain is valid:", my_blockchain.is_chain_valid(my_blockchain.chain))   