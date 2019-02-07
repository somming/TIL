from random import randint

#노드 정의하기
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None


class LinkedList:
	def __init__(self):
		HeadNode = Node("HEAD")
		self.head = HeadNode
		self.tail = HeadNode
		self.numofdata = 0

	def 
