class Node:
    """
    Represents a single node in a singly linked list.

    Attributes:
        value: The data stored in the node.
        next: A reference to the next node in the list, or None if it's the tail.
    """

    def __init__(self, value):
        """
        Initializes a new node with the given value.

        Args:
            value: The value to store in the node.
        """

        self.value = value
        self.next = None
    
class LinkedList:
    """
    Implements a singly linked list with custom iterators.

    Attributes:
        head: A reference to the first node in the list, or None if the list is empty.
    """

    def __init__(self):
        """
        Initializes an empty linked list.
        """

        self.head = None
        
    def __iter__(self):
        """
        Returns a LinkedListIterator object to enable iteration over the list.

        Returns:
            A LinkedListIterator object.
        """

        return LinkedListIterator(self.head)
        
    def add(self, value):
        """
        Adds a new node with the given value to the beginning of the list.

        Args:
            value: The value to add to the list.
        """

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    def remove(self, value):
        """
        Removes the first node with the given value from the list.

        Args:
            value: The value to remove from the list.

        Raises:
            ValueError: If the value is not found in the list.
        """

        current = self.head
        previous = None
        
        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                
                return
        
        previous = current
        current = current.next
        
        raise valueError("Value not found in linked list")
    
class LinkedListIterator:
    """
    Custom iterator for the LinkedList class.

    Attributes:
        current: A reference to the current node in the iteration.
    """

    def __init__(self, head):
        """
        Initializes the iterator with the head of the list.

        Args:
            head: The head node of the list to iterate over.
        """

        self.current = head
        
    def __iter__(self):
        """
        Returns itself as an iterator.

        Returns:
            The LinkedListIterator object itself.
        """

        return self
        
    def __next__(self):
        """
        Returns the value of the current node and advances to the next node.

        Raises:
            StopIteration: If there are no more nodes to iterate over.

        Returns:
            The value of the current node.
        """
        
        if not self.current:
            raise StopIteration
        else:
            value = self.current.value
            self.current = self.current.next
        
        return value
    
# Create a linked list
linked_list = LinkedList()

# Add some elements
linked_list.add(1)
linked_list.add(0)
linked_list.add(3)

try:
    linked_list.remove(3)
except valueError as e:
    print(e)

# Iterate over the list using the custom iterator
for value in linked_list:
    print(value)  # Output: 3 2 1