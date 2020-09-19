"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def __repr__(self):
        return f'{self.value}'
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        # check if list is empty
        if self.length == 0:
            # set the node as the head and tail
            self.head = new_node
            self.tail = new_node
            # increase length
            self.length += 1
        else:
            # make the current head's previous node the new head
            self.head.prev = new_node
            # set the new nodes next as the current head
            new_node.next = self.head
            # set the new node as the head of the list
            self.head = new_node
            # increase length
            self.length += 1


        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return "Cannot remove items from an empty list."
        elif self.length == 1:
            # make the list empty if there's only one item
            value = self.head.value
            self.tail = None
            self.head = None
            self.length -= 1
            return value
        else:
            value = self.head.value
            new_head = self.head.next
            # change the new head to have no previous node
            new_head.prev = None
            # overwrite the old head
            self.head = new_head
            # decrease length
            self.length -= 1
            # return the value of the old head
            return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        # check if list is empty
        if self.length == 0:
            # set the node as the head and tail
            self.head = new_node
            self.tail = new_node
            # increase length
            self.length += 1

        else:
            # make the current tail's next node the new node
            self.tail.next = new_node
            # set the new nodes previous as the current tail
            new_node.prev = self.tail
            # set the new node as the tail of the list
            self.tail = new_node
            # increase length
            self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            return "Cannot remove items from an empty list."
        elif self.length == 1:
            # make the list empty if there's only one item
            value = self.tail.value
            self.tail = None
            self.head = None
            self.length -= 1
            return value
        else:
            value = self.tail.value
            new_tail = self.tail.prev
            # change the new tail to have no next node
            new_tail.next = None
            # overwrite the old tail
            self.tail = new_tail
            # decrease length
            self.length -= 1
            # return the value of the old head
            return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.length == 0:
            return "List is empty"
        elif node == self.head:
            return 'Node is already at the front'
        elif node == self.tail:
            # overwrite the tail to be the previous one
            self.tail = node.prev
            # change the new tail to have no next
            self.tail.next = None
            # set the current head's prev to be the node
            self.head.prev = node
            node.next = self.head
            # overwrite the head to be the node
            self.head = node
        else:
            # get the prev and next nodes for that node
            previous_node = node.prev
            next_node = node.next
            # link the two together
            previous_node.next = next_node
            next_node.prev = previous_node
            
            self.head.prev = node
            node.next = self.head
            self.head = node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.length == 0:
            return "List is empty"
        elif node == self.tail:
            return 'Node is already at the end'
        elif node == self.head:
            # overwrite the head to be the head.next
            self.head = node.next
            # change the new head to have no prev
            self.head.prev = None
            # set the current tail's next to be the node
            self.tail.next = node
            # set node.next as the current tail
            node.prev = self.tail
            # overwite the tail
            self.tail = node
        else:
            previous_node = node.prev
            next_node = node.next
            previous_node.next = next_node
            next_node.prev = previous_node
            
            self.tail.next = node
            node.prev = self.tail
            self.tail = node


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            previous_node = node.prev
            next_node = node.next
            previous_node.next = next_node
            next_node.prev = previous_node
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        values = [self.head.value]
        node = self.head
        while node != self.tail:
            values.append(node.next.value)
            node = node.next

        return max(values)

