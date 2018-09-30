# Lowest Common Ancestor unit test
import pytest
import binary_tree as bt
import lca 
from random import randint

@pytest.fixture
def rand_tree():
	tree = bt.Tree()
	for i in range(25):
		tree.add(randint(1,50))
	return tree

@pytest.fixture
def empty_tree():
	tree = bt.Tree()
	return tree

def test_lca(empty_tree, rand_tree):
	# assert function returns -1 for empty tree
	assert lca.find_lca(empty_tree.root, 4, 5) == -1
	
	# assert returns root for lca of root.left and root.right
	assert lca.find_lca(rand_tree.root, rand_tree.root.left, rand_tree.root.right) == rand_tree.root
