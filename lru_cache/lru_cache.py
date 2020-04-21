# LRU is Least Recently Used
# it's a cache eviction policy
# when we have a loose collection of items and we want to remove items in a certain order
# similar to FIFO policy, or queue system. except we're using it for a cache
# when size limit is met, must evict an item, this should be the least recently used item
# if an item is accessed, it is moved to the front of the list
# this makes it the last to be removed in the event of exceeding the limit
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.dll = DoublyLinkedList()
        self.size = 0
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.storage.keys():
            self.dll.move_to_front(self.storage[key])
            return self.storage[key].value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if key in self.storage:
            self.storage[key].value = (key, value)
            self.dll.move_to_front(self.storage[key])
            return

        elif key not in self.storage:
            new_node = self.dll.add_to_head((key, value))
            self.storage[key] = new_node
            self.size += 1

            if self.size > self.limit:
                self.size -= 1
                old = self.dll.remove_from_tail()
                del self.storage[old[0]]
