#!/usr/bin/env python3
"""basic cache """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """basic dictionnary"""

    def put(self, key, item):
        """put new value into cache_data dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get value of cache_data dictionary"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
