# Lowest Common Ancestor unit test
import pytest
import tree as t

@pytest.fixture
def empty_tree():
	empty_tree = t.Tree()
	return empty_tree

# Tree data structure tests
def test_initialisation(empty_tree):
	assert empty_tree.getRoot == None

def test_add(empty_tree):
	empty_tree.add(0)
	assert empty_tree.getRoot == 0
