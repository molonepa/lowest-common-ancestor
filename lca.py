import binary_tree as bt
# Finds path from root to node n
# Returns True if path exists, otherwise False
def findPath(root, path, n):
	if root == None:
		return False

	path.append(root.data)

	if root.data == n:
		return True

	if((root.left != None and findPath(root.left, path, n)) or (root.right != None and findPath root.right, path, n)):
		return True

	path.pop()
	return False

# Finds lowest common ancestor of nodes n1 and n2
# Returns LCA if n1 and n2 are present in the tree, otherwise -1
def find_lca(root, n1, n2):
	path1 = []
	path2 = []

	if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
		return -1

	i = 0
	while(i < len(path1) and i < len(path2)):
		if path1[i] != path2[i]:
			break
		i += 1
	return path1[i-1]
