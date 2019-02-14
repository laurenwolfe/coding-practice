from trees import binary_tree
from lists.linked_list import build_linked_list, LinkedList
from collections import deque


def build_tree_from_linked_list(head):
    """Converts a linked list to binary tree.
    Add nodes to queue as they're traversed. Popped value is current
    root.
    """
    tree_queue = deque()
    tree = binary_tree.BinaryTree()

    if not head:
        tree.root = None
        return

    tree.root = binary_tree.Node(head.data)
    tree_queue.append(tree.root)
    head = head.next

    while head:
        parent = tree_queue.popleft()
        r_child = None
        l_child = binary_tree.Node(head.data, parent)
        tree_queue.append(l_child)
        head = head.next

        if head:
            r_child = binary_tree.Node(head.data, parent)
            tree_queue.append(r_child)
            head = head.nextß

        parent.left = l_child
        parent.right = r_child

    return tree


def traversal(root):
    """Basic form for traversal."""
    if root is not None:
        # print("preorder: ", root.data)
        traversal(root.left)
        # print("inorder: ", root.data)
        traversal(root.right)
        # print("postorder: ", root.data)


def find_height(root, height):
    if not root:
        return height
    else:
        return find_height(root.left, height + 1)


def breadth_first_traversal(tr_queue, level, build_str):
    """Print a graphical depiction of the tree using breadth first traversal."""
    if len(tr_queue) == 0:
        return

    root = tr_queue.popleft()
    build_str = build_str + "{0:4d}".format(root.data)

    if root.data == 2**level - 1:  # reached a new level of tree
        print_str = "{: ^50}\n".format(build_str)
        build_str = ""
        print(print_str)
        level = level + 1

    if root.left:
        tr_queue.append(root.left)
    if root.right:
        tr_queue.append(root.right)

    breadth_first_traversal(tr_queue, level, build_str)


if __name__ == "__main__":
    """Generate linked list, convert to binary tree."""
    l_list = build_linked_list(24, 1, LinkedList())
    bin_tree = build_tree_from_linked_list(l_list.head)

    queue = deque()
    queue.append(bin_tree.root)
    breadth_first_traversal(queue, 1, "")
