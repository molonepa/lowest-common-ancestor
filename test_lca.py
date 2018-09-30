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
	assert find_lca(empty_tree.getRoot, 4, 5) == -1
	
