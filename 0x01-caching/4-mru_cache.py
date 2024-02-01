#!/usr/bin/env python3
"""Caching system using MRU algorithm."""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Most Recently Used (MRU) caching system.
    Inherits from BaseCaching and implements MRU algorithm for caching.
    Methods:
        put(key, item): Add an item in the cache with MRU algorithm.
        get(key): Get an item by key.
    """

    def __init__(self):
        """Initialize MRUCache instance.
        Initialize the cache data dictionary and keys list.
        """
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """Add an item in the cache with MRU algorithm.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS, discard the most recently used item
        (MRU algorithm). You must print 'DISCARD: {key}' with the key
        discarded and following by a new line."""
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__keys:
            discard = self.__keys.pop()
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))
        if key and item:
            if key not in self.__keys:
                self.__keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key
        Returns:
            any: Value associated with the key in the cache or
            None if the key is not present in the cache.
        """
        if not key or key not in self.cache_data:
            return None
        self.__keys.remove(key)
        self.__keys.append(key)
        return self.cache_data[key]
