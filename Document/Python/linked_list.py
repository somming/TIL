class Node:
	def __init__(self,data=None):
		self.__data = data
		self.__next = None

	def __del__(self):
		print("data of {} is deleted".format(self.data))

	@property
	def data(self):
		return self.__data
	

	@data.setter
	def data(self,data):
		self.__data = data

	@property
	def next(self):
		return self.__next

	@next.setter
	def next(self,n):
		self.__next = n

class Linked_list:
	def __init__(self):
		self.head = None
		self.tail = None
		self.d_size = 0
	
	def empty(self):
		if self.d_size == 0:
			return True
		else:
			return False

	def size(self):
		return self.d_size

	def append(self,data):
		new_node = Node(data)
		if self.empty():
			self.head = new_node
			self.tail = new_node
			self.d_size += 1
		else:
			self.tail.next = new_node
			self.tail = new_node
			self.d_size += 1

	def search_target(self,target,start=0):
		'''
		start로부터 target과 일치하는 첫 번째 데이터와 그 위치를 반환
		target이 존재하지 않을 때:->(None,None)
		'''

		if self.empty():
			return None

		pos = 0
		cur = self.head

		if pos >= start and target == cur.data:
			return cur.data, pos

		while cur.next:
			pos += 1
			cur = cur.next

			if pos >= start and target == cur.data:
				return cur.data, pos

		return None,none

	def search_pos(self,pos):
		'''
		search_pos(pos) -> data
		pos가 범위를 벗어날 때 -> None
		'''

		if pos > self.size() - 1:
			return None

		cnt = 0
		cur = self.head
		if cnt == pos:
			return cur.data

		while cnt < pos:
			cur = cur.next
			cnt += 1

		return cur.data

	def remove(self,target):
		if self.empty():
			return None

		bef = self.head
		cur = self.head

		#삭제 노드가 첫 번째 노드일 때
		if target == cur.data:
			#data가 하나일 때
			if self.size() == 1:
				self.head = None
				self.tail = None
			#data가 여러 개일 때 
			else:
				self.head = self.head.next

			self.d_size -= 1
			return cur.data

		while cur.next:
			bef = cur
			cur = cur.next

			#삭제 노드가 첫 번째 노드가 아닐 때
			if target == cur.data:
				#삭제 노드가 마지막 노드일 때
				if cur == self.tail:
					self.tail = bef

				#일반적인 경우
				bef.next = cur.next
				self.d_size -= 1
				return cur.data

		return None

def show_list(slist):
		if slist.empty():
			print('The list is empty')
			return

		for i in range(slist.size()):
			print(slist.search_pos(i),end='  ')	