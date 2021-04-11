import pytest

import solution


class TestBinaryTree:
    @pytest.fixture(autouse=True)
    def _setup(self):
        self.binary_tree = solution.BinaryTree()
        self.node1 = solution.BinaryTreeNode(key=1)
        self.node4 = solution.BinaryTreeNode(key=4)
        self.node7 = solution.BinaryTreeNode(key=7)
        self.node6 = solution.BinaryTreeNode(key=6, left=self.node4, right=self.node7)
        self.node3 = solution.BinaryTreeNode(key=3, left=self.node1, right=self.node6)
        self.node13 = solution.BinaryTreeNode(key=13)
        self.node14 = solution.BinaryTreeNode(key=14, left=self.node13)
        self.node9 = solution.BinaryTreeNode(key=9)
        self.node10 = solution.BinaryTreeNode(key=10, right=self.node14, left=self.node9)
        self.root = solution.BinaryTreeNode(key=8, left=self.node3, right=self.node10)

    def test_is_balanced(self):
        assert self.binary_tree.is_balanced(self.root) is True

    def test_find_min_key(self):
        assert self.binary_tree.find_min_key(self.root) == 1

    def test_find_max_key(self):
        assert self.binary_tree.find_max_key(self.root) == 14

    def test_search_for_node(self):
        assert self.binary_tree.search_for_node(self.root, key_to_search_for=13).key == 13

    def test_next_key(self):
        assert self.binary_tree.next_key(self.root, key_to_search_for=8) == 9

    # Check insertion place
    def test_insert_node(self):
        parent = self.binary_tree.insert_node(self.root, 5)
        assert parent.key == 4 and parent.right.key == 5

    def test_in_order_traversal(self):
        assert self.binary_tree.in_order_traversal(self.root) == [8, 3, 1, 6, 4, 7, 10, 9, 14, 13]
