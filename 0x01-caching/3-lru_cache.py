#!/usr/bin/env python3
"""LRU caching
"""
from base_caching import BaseCaching
import time


class LRUCache(BaseCaching):
    """Defines a LRUCache class
    """
    timeStamp = {}

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assigns to the dictionary self.cache_data
           based on LRU algorithm
        """
        if key is None or item is None:
            return
        if len(self.cache_data) == 0:
            self.cache_data[key] = item
            LRUCache.timeStamp[key] = time.time()
            return

        if key in self.cache_data.keys():
            self.cache_data[key] = item
            LRUCache.timeStamp[key] = time.time()
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least = list(LRUCache.timeStamp.values())[0]
            removed_key = list(LRUCache.timeStamp.keys())[0]
            for rm_key, lst in LRUCache.timeStamp.items():
                if lst < least:
                    least = lst
                    removed_key = rm_key
            del self.cache_data[removed_key]
            del LRUCache.timeStamp[removed_key]
            print(f"DISCARD: {removed_key}")
        self.cache_data[key] = item
        LRUCache.timeStamp[key] = time.time()

    def get(self, key):
        """ return the value in self.cache_data """
        if key is None or key not in self.cache_data.keys():
            return None
        LRUCache.timeStamp[key] = time.time()
        return self.cache_data[key]
