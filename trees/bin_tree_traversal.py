from trees import binary_tree
from lists.linked_list import build_linked_list, LinkedList
from collections import deque


def build_tree_from_list(head):
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
            head = head.next

        parent.left = l_child
        parent.right = r_child

    return tree


def traversal(root):
    if root is not None:
        # print("preorder: ", root.data)
        traversal(root.left)
        # print("inorder: ", root.data)
        traversal(root.right)
        # print("postorder: ", root.data)


def find_height(root, height):
    if root:
        find_height(root.left, height + 1)
    return height


def breadth_first_traversal(tr_queue, level):
    if len(tr_queue) == 0:
        return

    root = tr_queue.popleft()

    print(root.data, end=" ")
    if root.data == 2**level - 1:
        print()
        level = level + 1

    if root.left:
        tr_queue.append(root.left)
    if root.right:
        tr_queue.append(root.right)

    breadth_first_traversal(tr_queue, level)


if __name__ == "__main__":
    l_list = build_linked_list(16, 1, LinkedList())
    bin_tree = build_tree_from_list(l_list.head)
#    traversal(bin_tree.root)

    queue = deque()
    queue.append(bin_tree.root)
    print(bin_tree.root.data)
    breadth_first_traversal(queue, 1)
    print("height: ", find_height(bin_tree.root, 1))
