#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        length = 0
        node = self.head

        while node is not None:
            length += 1
            node = node.next

        return length

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        node = Node(item)
        # TODO: Append node after tail, if it exists
        if self.head is not None:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node



    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        node = Node(item)
         # TODO: Prepend node before head, if it exists
        if self.head is not None:
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node

    def find(self, quality):
        """ Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) If we find the data in the first node
        Worst case running time: O(n) If data isnt found at all """
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        node = self.head
        while node is not None:
            if quality(node.data):
                return node.data
            else:
                node = node.next


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # found = False
        previous = None
        node = self.head

        while node is not None:
            if node.data == item:
                # We found the node!
                if previous is not None:
                    if node == self.tail:
                        self.tail = previous
                        self.tail.next = None
                    else:
                        previous.next = node.next
                elif node == self.head:
                    self.head = node.next
                    if node.next is None:
                        self.tail = None
                return
            else:
                previous = node
                node = node.next
                
        raise ValueError('Item not found: {}'.format(item))
    
    def replace(self, item, value, all=False):
            """Finds and replaces a value in the linked list"""
            node = self.head
            previous = None
            while node is not None:
                if node.data == item:
                    new_node = Node(value)
                    new_node.next = node.next
                    if node == self.head:
                        self.head = new_node
                    if node == self.tail:
                        self.tail = new_node
                    if previous is not None:
                        previous.next = new_node
                    if not all:
                        break
                previous = node
                node = node.next

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
