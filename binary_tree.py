# Binary Tree data structure to be used in lowest common ancestor assignment

# Node definition
class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

# Tree definiton
class Tree:
	def __init__(self):
		self.root = None

	def add(self, data):
		if(self.root == None):
			self.root = Node(data)
		else:
			self._add(data, self.root)

	# Private function used by add() when tree has more than one node
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

	# Function takes data as parameter and returns node with matching data
	def get(self, data):
		if(self.root != None):
			return self._get(data, self.root)
		else:
			return None

	# Private function used by get()when tree has more than one node
	def _get(self, data, node):
		if(data == node.data):
			return node
		elif(data < node.data and node.left != None):
			self._get(data, node.left)
		elif(data > node.data and node.right != None):
			self._get(data, node.right)
