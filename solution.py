class BinaryTreeNode:
    def __init__(self, key=0, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return 'TreeNode#{}'.format(self.key)


class BinaryTree:
    def __init__(self):
        self.traversal_route = []

    def max_depth(self, root):
        if not root:
            return 0
        left_height = self.max_depth(root.left)
        right_height = self.max_depth(root.right)

        if abs(left_height - right_height) > 1:
            return 0
        return max(left_height, right_height) + 1

    def is_balanced(self, root: BinaryTreeNode) -> bool:
        return bool(self.max_depth(root))

    def in_order_traversal(self, root: BinaryTreeNode):
        if root:
            self.traversal_route.append(root.key)
            self.in_order_traversal(root.left)
            self.in_order_traversal(root.right)
        return self.traversal_route

    def search_for_node(self, root: BinaryTreeNode, key_to_search_for) -> BinaryTreeNode:
        if not root or key_to_search_for == root.key:
            return root
        if root.key < key_to_search_for:
            return self.search_for_node(root.right, key_to_search_for)
        return self.search_for_node(root.left, key_to_search_for)

    def find_min_key(self, root: BinaryTreeNode):
        if not root.left:
            return root.key
        return self.find_min_key(root.left)

    def find_max_key(self, root: BinaryTreeNode):
        if not root.right:
            return root.key
        return self.find_max_key(root.right)

    def next_key(self, root: BinaryTreeNode, key_to_search_for):
        current = root
        successor = None
        while current:
            if current.key > key_to_search_for:
                successor = current
                current = current.left
            else:
                current = current.right
        return successor.key

    def insert_node(self, root: BinaryTreeNode, key_to_insert):
        if not root:
            return BinaryTreeNode(key=key_to_insert)
        if root.key < key_to_insert:
            root.right = self.insert_node(root.right, key_to_insert)
        elif root.key > key_to_insert:
            root.left = self.insert_node(root.left, key_to_insert)

        self.traversal_route.append(root)
        return self.traversal_route[0]
