#!/usr/bin/python3
"""
Task 5. LFU Caching

Class LFUCache inheriting BaseCaching
"""

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """FIFOCache
    """

    def __init__(self):
        """__init__

        Initialize class instance.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self._frequency_dict = {}

    def put(self, key, item):
        """put

        This method puts an item with it's key if they're valid.

        Arguments:
            key (str): The key to place in the dictionary with the item.
            item (str): The item to place in the dictionary linked to the key.
        """
        if key is None or item is None:
            return

        frecuency = self._frequency_dict.get(key, 0)
        if key in self.cache_data:
            del self._frequency_dict[key]
            del self.cache_data[key]
        self._frequency_dict[key] = frecuency + 1
        self.cache_data[key] = item

        if len(self.cache_data) <= BaseCaching.MAX_ITEMS:
            return

        for k in sorted(self._frequency_dict, key=self._frequency_dict.get):
            if k != key:
                discard = k
                del self.cache_data[k]
                print(f"DISCARD: {discard}")
                del self._frequency_dict[k]
                break

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
        item = self.cache_data.get(key)
        if item:
            del self.cache_data[key]
            self.cache_data[key] = item

            frecuency = self._frequency_dict.get(key)
            del self._frequency_dict[key]
            self._frequency_dict[key] = frecuency + 1
        return item