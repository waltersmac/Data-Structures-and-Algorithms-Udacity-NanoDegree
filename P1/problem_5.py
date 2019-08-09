import hashlib
from datetime import datetime


class Block:

	def __init__(self, timestamp, data, previous_hash):
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.calc_hash()
		self.next = None
		self.previous = None


	def calc_hash(self):
		sha = hashlib.sha256()
		string = self.data
		hash_str = string.encode('utf-8')
		sha.update(hash_str)

		return sha.hexdigest()



class BlockChain(object):

	def __init__(self):
		self.head = None
		self.tail = None
        
	def append(self, timestamp, data):
		
		if self.head is None:
			self.head = Block(timestamp, data, 0)
			self.tail = self.head
			return

		
		self.tail.next = Block(timestamp, data, str(self.tail.hash))
		self.tail.next.previous = self.tail
		self.tail = self.tail.next
		return



timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

chain = BlockChain()
chain.append(timestamp, "Block")
chain.append(timestamp, "Block2")
chain.append(timestamp, "Block3")
chain.append(timestamp, "Block4")


block = chain.head
while block:
    print([block.timestamp, block.data, block.hash, block.previous_hash])
    block = block.next





