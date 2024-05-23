#!/usr/bin/python3
"""
Task 4. MRU Caching

Class MRUCache inheriting BaseCaching
"""

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """FIFOCache
    """

    def __init__(self):
        """__init__

        Initialize class instance.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self._mru = ""

    def put(self, key, item):
        """put

        This method puts an item with it's key if they're valid.

        Arguments:
            key (str): The key to place in the dictionary with the item.
            item (str): The item to place in the dictionary linked to the key.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key in self.cache_data:
                self.cache_data.update({key: item})
                self._mru = key
            else:
                # discard the most recently used item
                discarded = self._mru
                del self.cache_data[discarded]
                print("DISCARD: {}".format(discarded))
                self.cache_data[key] = item
                self._mru = key
        else:
            self.cache_data[key] = item
            self._mru = key

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
        if key in self.cache_data:
            self._mru = key
            return self.cache_data.get(key)