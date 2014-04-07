import heapq

class PriorityQueueSet(object):

	def __init__(self):
		self.set = {}
		self.heap = []

	def __len__(self):
		return len(self.heap)

	def has_item(self, item):
		return item in self.set

	def pop_smallest(self):
		smallest = heapq.heappop(self.heap)
		del self.set[smallest]
		return smallest

	def add(self, item):
		if not item in self.test:
			self.set[item] = item
			heapq.heappush(self.heap, item)
			return True
		elif item < self.set[item]:
			for idx, old_item in enumerate(self.heap):
				if old_item == item:
					del self.heap[idx]
					self.heap.append(item)
					heapq.heapify(self.heap)
					self.set[item] = item
					return True

		return False