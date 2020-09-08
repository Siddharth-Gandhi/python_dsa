# LOWER LEVEL PROTOCOL:
# each node has at max 2 nodes
# meaning local constraints

# HIGHER LEVEL PROTOCOL:
# "search" every node to the left of a node has values <
# the current node value. So the constraint isn't just on one node but
# multiple nodes at the same time

# full bst: where all non - leaf nodes have 2 nodes and leaf have none
# complete bst: every level is full except last one and in that all nodes
# are as left as possible

# balanced bst: none of the leafs can be more than a single level away than
# any other leaves
# balanced bsts have search, ins and del more efficient

# self balancing bst: directly balances when add and del -> complex


class node:
    # user never uses this
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class binary_search_tree:
    # integers only
    # _ are private fns: notation
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            # no left child
            if cur_node.left_child == None:
                cur_node.left_child = node(value)
            else:
                # recursively insert to the lefet subtree
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Value already in tree!")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            # inorder traversal
            # will give sorted order
            self._print_tree(cur_node.left_child)
            print(cur_node.value)
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_ht):
        if cur_node == None:
            return cur_ht
        left_height = self._height(cur_node.left_child, cur_ht + 1)
        right_height = self._height(cur_node.right_child, cur_ht + 1)
        return max(left_height, right_height)

    def make_rand_tree(self, num_ele=10, max_int=100):
        from random import randint

        for _ in range(num_ele):
            cur_elem = randint(0, max_int)
            self.insert(cur_elem)

    def make_tree_from_list(self, arr):
        for ele in arr:
            self.insert(ele)


tree = binary_search_tree()
tree.make_tree_from_list([1, 2, 3, 4, 5])
tree.print_tree()
print("Tree height is", tree.height())
