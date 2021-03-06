#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(n) checks all buckets and nodes to gather keys"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, _ in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(n) checks all buckets and nodes to gather values"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_vals = []
        for bucket in self.buckets:
            for _ , value in bucket.items():
                all_vals.append(value)
        return all_vals

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) checks all nodes"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(b) if each bucket has a property that contains it's length, otherwise O(n) to traverse all buckets and nodes"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        count = 0
        for bucket in self.buckets:
            count += bucket.length()
        return count
        
    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(1) if found at the beginning of the list of the first bucket else O(l) where l is the length of the matching bucket"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        value = bucket.find(lambda node: node[0] == key)
        if value is not None:
            return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(1) if found at the beginning of the list of the first bucket else O(l) where l is the length of the matching bucket"""
        index = self._bucket_index(key) # Find bucket where given key belongs
        bucket = self.buckets[index] 
        value = bucket.find(lambda node: node[0] == key) #  Check if key-value entry exists in bucket
        if value is not None:
            return value[1] #  If found, return value associated with given key
        raise KeyError('Key not found: {}'.format(key)) #  Otherwise, raise error to tell user get failed

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(1) if found at the beginning of the list of the first bucket else O(l) where l is the length of the matching bucket"""
        index = self._bucket_index(key) #  Find bucket where given key belongs
        bucket = self.buckets[index]
        original = bucket.find(lambda node: node[0] == key) #  Check if key-value entry exists in bucket
        if original is not None:
            bucket.replace(original, (key, value)) #  If found, update value associated with given key
        else:
            bucket.append((key, value)) #  Otherwise, insert given key-value entry into bucket

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(1) if found at the beginning of the list of the first bucket else O(l) where l is the length of the matching bucket"""
        index = self._bucket_index(key) #  Find bucket where given key belongs
        bucket = self.buckets[index]
        node = bucket.find(lambda node: node[0] == key) #  Check if key-value entry exists in bucket
        if node is not None:
            bucket.delete(node) #  If found, delete entry associated with given key
        else:
            raise KeyError('Key not found: {}'.format(key)) #  Otherwise, raise error to tell user delete failed


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
