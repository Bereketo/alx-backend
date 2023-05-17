#!/usr/bin/env python3
"""MRU caching
"""
from base_caching import BaseCaching
import time


class MRUCache(BaseCaching):
    """Defines a MRUCache class
    """
    timeStamp = {}

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assigns to the dictionary self.cache_data
           based on MRU algorithm
        """
        if key is None or item is None:
            return
        if len(self.cache_data) == 0:
            self.cache_data[key] = item
            MRUCache.timeStamp[key] = time.time()
            return

        if key in self.cache_data.keys():
            self.cache_data[key] = item
            MRUCache.timeStamp[key] = time.time()
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most = list(MRUCache.timeStamp.values())[0]
            removed_key = list(MRUCache.timeStamp.keys())[0]
            for rm_key, mst in MRUCache.timeStamp.items():
                if mst > most:
                    most = mst
                    removed_key = rm_key
            del self.cache_data[removed_key]
            del MRUCache.timeStamp[removed_key]
            print(f"DISCARD: {removed_key}")
        self.cache_data[key] = item
        MRUCache.timeStamp[key] = time.time()

    def get(self, key):
        """ return the value in self.cache_data """
        if key is None or key not in self.cache_data.keys():
            return None
        MRUCache.timeStamp[key] = time.time()
        return self.cache_data[key]
