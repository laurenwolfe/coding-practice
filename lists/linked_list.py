class LinkedList:
    def __init__(self):
        self.head = None


class LLNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None


def build_linked_list(idx_max, idx, lst):
    lst.head = LLNode(idx)
    build_ll_nodes(idx_max, idx + 1, lst.head)
    return lst


def build_ll_nodes(idx_max, idx, node):
    assert node is not False, "error, node None type in build_nodes"
    if idx < idx_max:
        node.next = LLNode(idx)
        build_ll_nodes(idx_max, idx + 1, node.next)


def print_list(l_list):
    cursor = l_list.head

    while cursor is not None:
        print(cursor.data)
        cursor = cursor.next
