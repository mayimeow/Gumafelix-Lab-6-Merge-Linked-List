class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

def merge_sorted_lists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return dummy.next

def print_linked_list(head):
    while head is not None:
        print(head.value, end=" -> ")
        head = head.next
    print()

# Example
list1 = LinkedList()
list1.add_node(1)
list1.add_node(2)
list1.add_node(4)

list2 = LinkedList()
list2.add_node(1)
list2.add_node(3)
list2.add_node(4)

result = merge_sorted_lists(list1.head, list2.head)
print("Merged List:", end=" ")
print_linked_list(result)
