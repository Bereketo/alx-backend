#!/usr/bin/env python3
"""LIFO caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Defines a LIFOCache class
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assigns to the dictionary self.cache_data """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            removed_key = list(self.cache_data.keys())[-1]
            del self.cache_data[removed_key]
            print(f"DISCARD: {removed_key}")
        self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
