#!/usr/bin/env python3
"""Caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Last In First Out"""

    def __init__(self):
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """put item into cache_data with LIFO algorithm"""
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__keys:
            discard = self.__keys.pop()
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))
        if key and item:
            self.__keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """get value of cache_data dictionary"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
