#!/usr/bin/python3
"""
Task 2. LIFO Caching

Class LIFOCache inheriting BaseCaching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """FIFOCache
    """

    def __init__(self):
        """__init__

        Initialize class instance.
        """
        super().__init__()
        self._last_item = ""

    def put(self, key, item):
        """put

        This method puts an item with it's key if they're valid.

        Arguments:
            key (str): The key to place in the dictionary with the item.
            item (str): The item to place in the dictionary linked to the key.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self._last_item)
            print("DISCARD: {}".format(self._last_item))
        self._last_item = key

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