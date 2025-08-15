class Node:

    def __init__(self, key):
        self.key = key
        self.value = None
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return f"({self.key}, {self.value})"


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def __contains__(self, key):
        current_node = self.root

        while current_node is not None:
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            else:
                return True

        return False

    def __iter__(self):
        yield from self._in_order_traversal(self.root)


    def __repr__(self):
        return str(list(self._in_order_traversal(self.root)))


    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key)
            self.root.value = value
        else:
            current_node = self.root
            while True:
                if key < current_node.key:
                    if current_node.left is None:
                        current_node.left = Node(key)
                        current_node.left.value = value
                        current_node.left.parent = current_node
                        break
                    else:
                        current_node = current_node.left
                elif key > current_node.key:
                    if current_node.right is None:
                        current_node.right = Node(key)
                        current_node.right.value = value
                        current_node.right.parent = current_node
                        break
                    else:
                        current_node = current_node.right
                else:
                    current_node.value = value
                    break


    def search(self, key):
        current_node = self.root

        while True:
            if current_node is None or key == current_node.key:
                return current_node
            elif key < current_node.key:
                if current_node.left is None:
                    return None
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    return None
                else:
                    current_node = current_node.right

    def delete(self, key):
        node = self.search(key)
        if node is None:
            raise KeyError("Key not found")
        self._delete(node)


    def traverse(self, order):
        if order  == 'inorder':
            yield from self._in_order_traversal(self.root)
        elif order == 'preorder':
            yield from self._pre_order_traversal(self.root)
        elif order == 'postorder':
            yield from self._post_order_traversal(self.root)
        else:
            raise ValueError("Unknown order")


    def _delete(self, node):

        if node.left is None and node.right is None:
            if node.parent is None:
                self.root = None
            else:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None

        elif node.left is None or node.right is None:
            child_node = node.left if node.left is not None else node.right

            if node.parent is None:
                child_node.parent = None
                self.root = child_node
            else:
                if node.parent.left == node:
                    node.parent.left = child_node
                else:
                    node.parent.right = child_node
            node.parent = node.left = node.right = None

        else:
            successor = self._successor(node)

            node.key = successor.key
            node.value = successor.value

            self._delete(successor)


    def _successor(self, node):
        if node is None:
            raise ValueError("")
        else:
            if node.right is None:
                return None
            current_node = node.right
            while current_node.left is not None:
                current_node = current_node.left
            return current_node


    def _in_order_traversal(self, node):
        if node is not None:
            yield from self._in_order_traversal(node.left)
            yield (node.key, node.value)
            yield from self._in_order_traversal(node.right)


    def _pre_order_traversal(self, node):
        if node is not None:
            yield (node.key, node.value)
            yield from self._in_order_traversal(node.left)
            yield from self._in_order_traversal(node.right)


    def _post_order_traversal(self, node):
        if node is not None:
            yield from self._in_order_traversal(node.left)
            yield from self._in_order_traversal(node.right)
            yield (node.key, node.value)


if __name__ == "__main__":
    
    bst = BinarySearchTree()
    
    bst.insert(10, 'x')
    bst.insert(5, 'x')
    bst.insert(2, 'x')
    bst.insert(9, 'x')
    bst.insert(22, 'x')
    
    
    print(list(bst._in_order_traversal(bst.root)))
    print(list(bst._pre_order_traversal(bst.root)))
    print(list(bst._post_order_traversal(bst.root)))
