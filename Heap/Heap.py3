# Heap class implementation

class Heap:
	def __init__(self) -> None:
		self.capacity = 10
		self.size = 0
		self.items = [0 for _ in range(self.capacity)]

	def get_left_child_index(self, parent_index: int) -> int:
		return parent_index*2 + 1 

	def get_right_child_index(self, parent_index: int) -> int:
		return parent_index*2 + 2

	def get_parent_index(self, child_index: int) -> int:
		return (child_index - 1) // 2

	def has_left_child(self, index) -> bool:
		self.get_left_child_index(index) < self.size

	def has_right_child(self, index) -> bool:
		self.get_right_child_index(index) < self.size

	def has_parent(self, index) -> bool:
		return self.get_parent_index(index) >= 0

	def left_child(self, parent_index: int) -> int:
		return self.items[self.get_left_child_index(parent_index)] 

	def right_child(self, parent_index: int) -> int:
		return self.items[self.get_right_child_index(parent_index)]

	def parent(self, child_index: int) -> int:
		return self.items[self.get_parent_index(child_index)]

	def swap(self, index_one, index_two) -> None:
		temp = self.items[index_one]
		self.items[index_one] = self.items[index_two]
		self.items[index_two] = temp

	def ensure_extra_capacity(self) -> None:
		if self.size > self.capacity:
			self.items.extend([0 for _ in range(self.capacity)])
			self.capacity = self.capacity * 2

	def peek(self) -> int:
		if self.size > 0:
			return self.items[0]

	def poll(self) -> int:
		if self.size > 0:
			item = self.items[0]
			self.items[0] = self.items[self.size - 1]
			self.size = self.size - 1
			self.heapify_down()
			return item

	def add(self, item: int) -> None:
		self.ensure_extra_capacity()
		self.items[self.size] = item
		self.size += 1
		self.heapify_up()

	def heapify_up(self) -> None:
		index = self.size - 1
		while self.has_parent(index) and self.parent(index) > self.items[index]:
			self.swap(index, self.get_parent_index(index))
			index = self.get_parent_index(index)

	def heapify_down(self) -> None:
		index = 0
		# If no left child, then definitely no right child.
		while self.has_left_child(index):
			# Get the smaller child index.
			smaller_child_index = self.get_left_child_index(index)
			if self.has_right_child() and self.right_child() < self.left_child():
				smaller_child_index = self.get_right_child_index()

			# Make the heap property to be fulfilled.
			if self.items[index] < self.items[smaller_child_index]:
				return
			else:
				self.swap(index, smaller_child_index)
				index = smaller_child_index 

	def print_heap(self) -> None:
		for item in self.items:
			if item != 0:
				print(item)


if __name__ == "__main__":
	heap = Heap() 
	heap.add(15)
	heap.add(20)
	heap.add(17)
	heap.add(10)
	heap.add(25)
	heap.add(13)
	heap.add(2)
	heap.print_heap()  # -> 2 15 10 20 25 17 13