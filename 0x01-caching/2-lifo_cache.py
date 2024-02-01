#!/usr/bin/env python3
"""Caching system using LIFO algorithm."""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Last In, First Out caching system.
    Inherits from BaseCaching and implements LIFO algorithm for caching.
    Methods:
        put(key, item) - Add an item in the cache with LIFO algorithm.
        get(key) - Get an item by key.
    """

    def __init__(self):
        """Initialize LIFOCache instance.
        Initialize the cache data dictionary and keys list.
        """
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """
        Add an item in the cache with LIFO algorithm.
        If the number of items in self.cache_data is higher
        than BaseCaching.MAX_ITEMS,
        discard the last item put in cache (LIFO algorithm)."""
        if len(self.cache_data) == BaseCaching.MAX_ITEMS and \
                key not in self.__keys:
            discard = self.__keys.pop()
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))
        if key and item:
            self.__keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key
        :return: any - value associated with the key in the cache
        or None if the key is not present in the cache"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
