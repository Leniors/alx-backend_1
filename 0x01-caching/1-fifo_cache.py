#!/usr/bin/python3
"""
Task 1. FIFO caching

Class FIFOCache inheriting BaseCaching
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache
    """

    def __init__(self):
        """__init__

        Initialize class instance.
        """
        super().__init__()

    def put(self, key, item):
        """put

        This method puts an item with it's key if they're valid.

        Arguments:
            key (str): The key to place in the dictionary with the item.
            item (str): The item to place in the dictionary linked to the key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = sorted(self.cache_data)[0]
            self.cache_data.pop(discard)
            print("DISCARD: {}".format(discard))

    def get(self, key):
        """get

        It gets the item linked to the key inputed if it's
        present in the cache.

        Arguments:
            key (str): The key to look for in the cache.

        Return:
            (str): The item linked to the key if found, None if not
                   found.
        """
        return self.cache_data.get(key)