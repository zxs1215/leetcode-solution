from leetcode import ListNode


def new_node(val, next):
    node = ListNode(val)
    node.next = next
    return node

def list_node_to_iter(n):
    while n is not None:
        yield n.val
        n = n.next


def list_node_from_iter(it):
    try:
        e = next(it)
    except StopIteration:
        return None

    node = ListNode(e)
    node.next = list_node_from_iter(it)
    return node
