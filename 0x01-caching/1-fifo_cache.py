#!/usr/bin/env python3
"""FIFO caching system."""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Frist In, First Out caching system.

    Inherits from BaseCaching and implements FIFO algorithm for caching.
    """

    def __init__(self):
        """Initialize FIFOCache instance.

        Initialize the cache data dictionary and keys list.
        """
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """Add an item in the cache.

        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS, discard the first item put in cache
        (FIFO algorithm).You must print 'DISCARD: {key}' with the key
        discarded and following by a new line.

        :param key: str - key to add to the cache
        :param item: any - item to add to the cache
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__keys:
            discard = self.__keys.pop(0)
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))
        if key and item:
            self.__keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key.

        :param key: str - key to retrieve value from the cache
        :return: any - value associated with the key in the cache
        or None if the key is not present in the cache
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
