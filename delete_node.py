"""
You’re given the pointer to the head node of a linked list and the position of a
node to delete. Delete the node at the given position and return the head node.
A position of 0 indicates head, a position of 1 indicates one node away from the
head and so on. The list may become empty after you delete the node.

Input Format
You have to complete the Node* Delete(Node* head, int position) method which
takes two arguments - the head of the linked list and the position of the node
to delete. You should NOT read any input from stdin/console. position will
always be at least 0 and less than the number of the elements in the list.

Output Format
Delete the node at the given position and return the head of the updated linked
list. Do NOT print anything to stdout/console.

"""


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Delete(head, position):
    if position == 0:
        new_head = head.next
        head.next = None
        return new_head
    else:
        index = 0
        curr = head
        while index < position - 1:
            curr = curr.next
            index += 1
        curr.next = curr.next.next
        return head
