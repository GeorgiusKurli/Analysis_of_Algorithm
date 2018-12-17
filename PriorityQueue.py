# nodes are [letter, number]

# priority queue that uses nodes
class PriorityQueue:

	# initialize the queue
	def __init__(self):
		self.queue = []

	# used for inserting item into queue
	def add(self, item = [], *args):
		if self.queue == []:
			self.queue.append(item)
			return
		
		else:
			for x in range(len(self.queue)):
				if self.queue[x][1] > item[1]:
					self.queue.insert(x, item)
					return

		self.queue.append(item)

	# used for popping from queue
	def pop(self):
		return self.queue.pop()

	# used to check if the queue is empty
	def empty(self):
		return self.queue == []

	# used to return the queue
	def return_all(self):
		return self.queue


# reverse priority queue that uses nodes
class ReversePriorityQueue:

	# initialize the queue
	def __init__(self):
		self.queue = []

	# used for inserting item into queue
	def add(self, item = [], *args):
		if self.queue == []:
			self.queue.append(item)
			return
		
		else:
			for x in range(len(self.queue)):
				if self.queue[x][1] < item[1]:
					self.queue.insert(x, item)
					return

		self.queue.append(item)

	# used for popping from queue
	def pop(self):
		return self.queue.pop()

	# used to check if the queue is empty
	def empty(self):
		return self.queue == []

	# used to return the queue
	def return_all(self):
		return self.queue

# priority queue testing
# test = PriorityQueue()
# print(test.empty())
# lista = ["a", 10]
# listb = ["b", 9]
# listc = ["c", 13]
# listd = ["d", 12]
# test.add(lista)
# test.add(listb)
# test.add(listc)
# test.add(listd)

# print(test.return_all())
# print(test.pop())