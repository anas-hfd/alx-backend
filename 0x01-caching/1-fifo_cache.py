#!/usr/bin/python3
"""Caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """a caching system using the FIFO algorithm
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) == self.MAX_ITEMS:
            discarded_key = list(self.cache_data.keys())[0]
            print("DISCARD: {}".format(discarded_key))
            del self.cache_data[discarded_key]

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None

        return self.cache_data.get(key)
