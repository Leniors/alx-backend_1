#!/usr/bin/python3
"""
Task 0. Basic dictionary

Class BasicCache inheriting BaseCaching
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache
    """

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