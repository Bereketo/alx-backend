#!/usr/bin/env python3
"""A caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic cache class
    """
    def put(self, key, item):
        """assigns to the dictionary  """
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """returns a value associated with key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
