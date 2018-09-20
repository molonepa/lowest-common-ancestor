class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

class Tree:
	def __init__(self):
		self.root = None

	def getRoot(self):
		return self.root

	def add(self, data):
		if(self.root == None):
			self.root = Node(data)
		else:
			self._add(data, self.root)

	def _add(self, data, node):
		if(data < node.data):
			if(node.left != None):
				self._add(data, node.left)
			else:
				node.left = Node(data)
		else:
			if(node.right != None):
				self._add(data, node.right)
			else:
				node.right = Node(data)

	def find(self, data):
		if(self.root != None):
			return self._find(data, self.root)
		else:
			return None

	def _find(self, data, node):
		if(data == node.data):
			return node
		elif(data < node.data and node.left != None):
			self._find(data, node.left)
		elif(data > node.data and node.right != None):
			self._find(data, node.right)
